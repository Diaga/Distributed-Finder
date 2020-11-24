from base.command import BaseCommand
from base.arguments import IntArgument


class PingCommand(BaseCommand):

    command = 'ping'
    arguments = [IntArgument()]

    def run(self):
        times = self.arguments[0].data
        for counter in range(1, times + 1):
            self.log(f'{counter}) Pong!', prefix=False)
