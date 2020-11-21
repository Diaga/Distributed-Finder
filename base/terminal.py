class BaseTerminal:
    """Handles the user input and handles matching commands"""

    def __init__(self, commands=None, prefix='finder %'):
        if commands is None:
            # Default argument should not be mutable
            commands = []

        self.prefix = prefix + ' '
        self.commands = commands

        for command in self.commands:
            command.log = self.log
            command.get_input = self.get_input

    def log(self, message, prefix=True):
        """Prints message to console with specified prefix"""
        if prefix:
            print(f'{self.prefix} {message}')
        else:
            print(message)

    def get_input(self, prompt=None):
        """Wrapper around input() to have a terminal like appearance"""
        if prompt is not None:
            self.log(f'{self.prefix} {prompt}')
        return input(f'{self.prefix} ')

    def run(self, welcome_message=None):
        """Runs the terminal in loop"""

        if welcome_message is not None:
            self.log(welcome_message, prefix=False)

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
