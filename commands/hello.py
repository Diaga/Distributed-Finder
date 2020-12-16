from base.command import BaseCommand


class HelloCommand(BaseCommand):
    """Print out the files and directories that presently
        exist in the directory user currently resides in.

        Usage: ls"""

    command = 'hello'

    def run(self):
        self.log('Hello World', prefix=False)
