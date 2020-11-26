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

    def __init__(self, commands=None, prefix='finder %'):
        if commands is None:
            # Default argument should not be mutable
            commands = []

        self.context = BaseTerminal.Context()
        self.prefix = prefix + ' '
        self.commands = []

        for command in commands:
            self.commands.append(command(
                context=self.context, log=self.log, get_input=self.get_input
            ))

    def log(self, message, prefix=True):
        """Prints message to console with specified prefix"""
        if prefix:
            print(f'{self.prefix} {message}')
        else:
            print(message)

    def get_input(self, prompt=None, prefix=True):
        """Wrapper around input() to have a terminal like appearance"""
        if prefix:
            if prompt is not None:
                self.log(f'{self.prefix} {prompt}')

            return input(f'{self.prefix} ')
        return input(f'{prompt}')

    def run(self):
        """Runs the terminal in loop"""

        latest_session = SessionDao.get_last_session()
        if latest_session is None:
            self.log('Welcome to Distributed Finder!', prefix=False)
            # make the sector divisions
            # should NOT be here
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
                        command.validate(arguments)
                        command.run()
                        break
                else:
                    self.log(f'terminal: command not found:'
                             f' {command_input}', prefix=False)
