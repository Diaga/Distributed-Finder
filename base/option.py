from abc import ABC


class Option(ABC):

    def __init__(self, option):
        if option == '':
            raise ValueError('Option cannot be blank!')

        self.option = option
        self.exists = False

    def validate(self, option):
        self.exists = option == self.option

    def __repr__(self):
        return self.option


class StringOption(Option):
    pass
