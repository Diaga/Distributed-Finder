from base.command import BaseCommand
from base.arguments import IntArgument
from base.option import StringOption


class PingCommand(BaseCommand):

    command = 'ping'
    arguments = [
        IntArgument(required=False, options=[
            StringOption('-r')
        ])
    ]

    def run(self):
        if self.arguments[0].has_validated:
            times = self.arguments[0].data

            for counter in range(1, times + 1):
                if self.arguments[0].options[0].exists:
                    self.log(f'{times + 1 - counter}) Pong!', prefix=False)
                else:
                    self.log(f'{counter}) Pong!', prefix=False)
        else:
            self.log('Pong!', prefix=False)
