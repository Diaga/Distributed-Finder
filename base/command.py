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

    def _check_input_length(self, arguments):
        length = 1

        for counter in range(len(arguments)):
            if arguments[counter][0] != '-' or counter < 1:
                if counter < len(self.arguments):
                    if self.arguments[counter].required:
                        length += 1
                else:
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

        counter = 0
        while counter != len(arguments):
            options = []
            for index in range(counter + 1, len(arguments)):
                if arguments[index][0] == '-' and counter < 2:
                    options.append(arguments[index])

            self.arguments[counter].validate(arguments[counter], options)
            counter += 1 + len(options)

    def run(self):
        pass
