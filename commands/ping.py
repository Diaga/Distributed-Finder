from base.command import BaseCommand
from base.arguments import IntArgument


class PingCommand(BaseCommand):

    command = 'ping'
    arguments = [IntArgument(required=False)]

    def run(self):
        if self.arguments[0].has_validated:
            times = self.arguments[0].data

            for counter in range(1, times + 1):
                self.log(f'{counter}) Pong!', prefix=False)
        else:
            self.log('Pong!', prefix=False)
