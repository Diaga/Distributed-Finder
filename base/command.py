from abc import ABC


class BaseCommand(ABC):
    """Base command for terminal
    Command Signature: <command> <arg1> <arg2> ...
    """

    command = None
    arguments = []
    options = []

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
            if arguments[counter][0] != '-':
                if counter < len(self.arguments):
                    if counter < len(self.arguments) and\
                            self.arguments[counter].required:
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
        user_counter = 0
        argument_started = False

        while user_counter != len(arguments):
            options = []

            if not argument_started:
                if arguments[user_counter][0] == '-':
                    for option in self.options:
                        if not option.exists:
                            option.validate(arguments[user_counter])
                else:
                    argument_started = True

                    if user_counter != len([
                        option for option in self.options if option.exists
                    ]):
                        raise ValueError('Command option does not exist!')

            if argument_started:
                for index in range(counter + 1, len(arguments)):
                    if arguments[index][0] == '-' and counter < 2:
                        options.append(arguments[index])

                self.arguments[counter].validate(
                    arguments[user_counter], options
                )
                counter += 1

            user_counter += 1 + len(options)

    def reset(self):
        for argument in self.arguments:
            argument.reset()

        for option in self.options:
            option.reset()

    def run(self):
        pass
