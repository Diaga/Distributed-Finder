from db.dao.sector_dao import SectorDao
from db.dao.directory_dao import DirectoryDao
from db.dao.session_dao import SessionDao
from db.models.session import Session
from db.base import sector_size, total_size


class BaseTerminal:
    """Handles the user input and handles matching commands"""

    class Context:
        """Holds the context for finder terminal"""

        def __init__(self):
            self.current_directory = DirectoryDao.get_root_directory()

        def parse_dir(self, path):
            """Parses path to a directory object
            :param path: Path to parse"""
            current_directory = self.current_directory

            split_path = path.split('/')

            # Check if user started the path from root
            if split_path[0] == '':
                current_directory = DirectoryDao.get_root_directory()
                split_path.pop(0)

            for level in split_path:
                if level == '..':
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

        self.context = BaseTerminal.Context()
        self.prefix = prefix
        self.commands = []

        for command in commands:
            self.commands.append(command(
                context=self.context, log=self.log, get_input=self.get_input
            ))

    @property
    def get_prefix(self):
        return f'{self.prefix} {self.context.current_directory} %'

    def log(self, message, prefix=True):
        """Prints message to console with specified prefix"""
        if prefix:
            print(f'{self.get_prefix} {message}')
        else:
            print(message)

    def get_input(self, prompt=None, prefix=True):
        """Wrapper around input() to have a terminal like appearance"""
        if prompt is not None:
            self.log(prompt, prefix=prefix)

        if prefix:
            return input(f'{self.get_prefix} ')
        return input()

    def run(self):
        """Runs the terminal in loop"""

        latest_session = SessionDao.get_last_session()
        if latest_session is None:
            self.log('Welcome to Distributed Finder!', prefix=False)
            SectorDao.create_sectors_division(
                total_size(), sector_size())

        else:
            self.log(latest_session, prefix=False)

        SessionDao.create_session(Session())

        while True:
            user_input = self.get_input()
            user_input_list = user_input.split(' ')
            if len(user_input_list) >= 1:
                command_input = user_input_list[0]
                arguments = user_input_list[1:]
                for command in self.commands:
                    if command.match(command_input):
                        try:
                            command.validate(arguments)
                            command.run()
                        except ValueError as e:
                            self.log(e, prefix=False)
                        break
                else:
                    self.log(f'terminal: command not found:'
                             f' {command_input}', prefix=False)
