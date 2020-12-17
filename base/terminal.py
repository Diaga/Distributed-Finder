import sys

from db.dao.sector_dao import SectorDao
from db.dao.directory_dao import DirectoryDao
from db.dao.session_dao import SessionDao
from db.dao.file_dao import FileDao

from db.models.session import Session
from db.base import SECTOR_SIZE, TOTAL_SIZE


class BaseTerminal:
    """Handles the user input and handles matching commands"""

    class Context:
        """Holds the context for finder terminal

        .. versionchanged: Lab 10: Allows context to be used as a context
        manager, allow context to access terminal using `terminal` property
        """
        def __init__(self, terminal):
            self.current_directory = DirectoryDao.get_root_directory()
            self.terminal = terminal

        def __enter__(self):
            self._sys_stdout = sys.stdout
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout = self._sys_stdout

        @staticmethod
        def set_stdout(file_handler):
            sys.stdout = file_handler

        def parse(self, path, is_file=False):
            """Parses path to a directory object
            :param path: Path to parse
            :param is_file: Specifies if we are looking for a file or
            directory"""
            current_directory = self.current_directory

            split_path = path.split('/')

            # Check if user started the path from root
            if split_path[0] == '':
                current_directory = DirectoryDao.get_root_directory()
                split_path.pop(0)

            for level in split_path:
                if level == '':
                    continue
                elif level == split_path[-1] and is_file:
                    file = FileDao.get_file_from_current_directory(
                        current_directory, level
                    )
                    if file is None:
                        raise ValueError('No such file exists!')

                    return file
                elif level == '..':
                    if current_directory.id != \
                            DirectoryDao.get_root_directory().id:
                        current_directory = current_directory.directory
                elif level == '.':
                    pass
                else:
                    directory = DirectoryDao.\
                        get_directory_from_current_directory(
                            current_directory, level
                        )
                    if directory is None:
                        raise ValueError('No such directory exists!')

                    current_directory = directory

            return current_directory

    def __init__(self, commands=None, prefix='finder'):
        if commands is None:
            # Default argument should not be mutable
            commands = []

        self.context = BaseTerminal.Context(terminal=self)
        self.prefix = prefix
        self.commands = []

        for command in commands:
            self.commands.append(command(
                context=self.context, log=self.log, get_input=self.get_input
            ))

    @property
    def get_prefix(self):
        return f'{self.prefix} {self.context.current_directory} %'

    def log(self, message, prefix=True, stdout=None):
        """Prints message to console with specified prefix"""
        if stdout is None:
            stdout = sys.stdout
        if prefix:
            print(f'{self.get_prefix} {message}', file=stdout)
        else:
            print(message, file=stdout)

    def get_input(self, prompt=None, prefix=True):
        """Wrapper around input() to have a terminal like appearance

        .. versionchanged: Lab 10: If output stream is not interactive,
        do nothing
        """
        if not sys.stdout.isatty():
            return

        if prompt is not None:
            self.log(prompt, prefix=prefix)

        if prefix:
            return input(f'{self.get_prefix} ')
        return input()

    def match_command(self, user_input):
        """Matches command input to one of the existing commands.

        :param user_input: Input to match
        :returns Matched command or None
        """
        inputs = user_input.strip().split('|')
        user_input_list = inputs[0].strip().split(' ')
        if len(user_input_list) >= 1:
            command_input = user_input_list[0]
            arguments = user_input_list[1:]

            for command in self.commands:
                if command.match(command_input):
                    return command, arguments, True, inputs[1:]

            return command_input, None, False, inputs[1:]

    def sansio_run(self, command, arguments, found=False):
        """Separate IO from run logic

        :param command: Command to execute
        :param arguments: Arguments to pass to command
        :param found: Whether command was found or error
        """
        if found:
            try:
                command.validate(arguments)
                command.run()
            except (ValueError, MemoryError) as e:
                self.log(e, prefix=False)
            finally:
                command.reset()
        else:
            self.log(f'terminal: command not found:'
                     f' {command}', prefix=False)

    def run(self):
        """Runs the terminal in loop"""

        latest_session = SessionDao.get_last_session()
        if latest_session is None:
            self.log('Welcome to Distributed Finder!', prefix=False)
            SectorDao.create_sectors_division(
                TOTAL_SIZE, SECTOR_SIZE)

        else:
            self.log(latest_session, prefix=False)

        SessionDao.create_session(Session())

        while True:
            user_input = self.get_input()

            command, arguments, found, _ = self.match_command(user_input)
            self.sansio_run(command, arguments, found)
