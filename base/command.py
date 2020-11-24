from abc import ABC


class BaseCommand(ABC):
    """Base command for terminal
    Command Signature: <command> <arg1> <arg2> ...
    """

    command = None
    arguments = []

    def __init__(self, context, log, get_input):
        self.context = context
        self.log = log
        self.get_input = get_input

    def __len__(self):
        """Returns required length of the command"""
        length = 1  # Length must at least be 1
        for argument in self.arguments:
            length += len(argument)

        return length

    @staticmethod
    def _check_input_length(arguments):
        length = 1
        for argument in arguments:
            if argument[0] != '-':
                length += 1

        return length

    def log(self, message, prefix=True):
        pass

    def get_input(self, prompt=None):
        pass

    def match(self, command):
        """Returns true if user input matches this command signature"""
        return command == self.command

    def validate(self, arguments):
        if self._check_input_length(arguments) != len(self):
            raise ValueError('Arguments length do not match!')

        for user_argument, argument in zip(arguments, self.arguments):
            argument.validate(user_argument)

    def run(self):
        pass
