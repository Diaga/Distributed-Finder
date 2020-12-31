from abc import ABC


class BaseArgument(ABC):

    def __init__(self, options=None, required=True):
        if options is None:
            options = []

        self._data = None
        self.options = options
        self.required = required
        self.has_validated = False

    def __len__(self):
        if self.required:
            return 1
        return 0

    def _parse(self, user_input, options=None):
        pass

    def _validate(self, user_input, options=None):
        if options:
            for user_option in options:
                for option in self.options:
                    if not option.exists:
                        option.validate(user_option)

            if len(options) != len([
                option for option in self.options if option.exists
            ]):
                raise ValueError('Option does not exists!')

        self._parse(user_input, options=options)
        self.has_validated = True

    @property
    def data(self):
        if self.has_validated:
            return self._data
        else:
            raise ValueError('Call validate() before accessing argument data')

    @data.setter
    def data(self, data):
        self.has_validated = True
        self._data = data

    def validate(self, user_input, options=None):
        self._validate(user_input, options=options)

    def reset(self):
        self.has_validated = False
        self._data = None

        for option in self.options:
            option.reset()


class IntArgument(BaseArgument):
    """Parses the argument as an integer"""

    def _parse(self, user_input, options=None):
        self._data = int(user_input)

    def validate(self, user_input, options=None):
        validation = user_input.isnumeric()
        if not validation:
            raise ValueError('Input is not numeric!')

        super(IntArgument, self).validate(user_input=user_input,
                                          options=options)


class StringArgument(BaseArgument):
    """Parses the argument as a result"""

    def _parse(self, user_input, options=None):
        self._data = user_input


class StaticArgument(BaseArgument):

    def __init__(self, arguments, options=None, required=False):
        super(StaticArgument, self).__init__(options=options,
                                             required=required)

        self.arguments = arguments

    def _parse(self, user_input, options=None):
        self._data = user_input

    def validate(self, user_input, options=None):
        validation = user_input in self.arguments
        if not validation:
            raise ValueError(f'Argument must be one of: {self.arguments}')

        super(StaticArgument, self).validate(user_input=user_input,
                                             options=options)
