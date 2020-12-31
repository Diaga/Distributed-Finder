from base.command import BaseCommand


class HelloCommand(BaseCommand):
    """Greets the world

        Usage: hello"""

    command = 'hello'

    def run(self):
        self.log('Hello World', prefix=False)
