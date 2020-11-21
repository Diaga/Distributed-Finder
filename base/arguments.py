from abc import ABC


class BaseArgument(ABC):

    def __init__(self, options=None):
        if options is None:
            options = []

        self._data = None
        self.options = options
        self.has_validated = False

    def __len__(self):
        return 1 + len(self.options)

    def _parse(self, user_input, options=None):
        pass

    def _validate(self, user_input, options=None):
        if options is not None:
            for user_option in options:
                for option in self.options:
                    option.validate(user_option)

        self._parse(user_input, options=options)
        self.has_validated = True

    @property
    def data(self):
        if self.has_validated:
            return self._data
        else:
            raise ValueError('Call validate() before accessing argument data')

    def validate(self, user_input, options=None):
        self._validate(user_input, options=options)


class IntArgument(BaseArgument):

    def _parse(self, user_input, options=None):
        self._data = int(user_input)

    def validate(self, user_input, options=None):
        validation = user_input.isnumeric()
        if not validation:
            raise ValueError('Input is not numeric!')

        super(IntArgument, self).validate(user_input=user_input,
                                          options=options)
