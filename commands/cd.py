from base.command import BaseCommand
from base.arguments import StringArgument


class CDCommand(BaseCommand):

    command = 'cd'
    arguments = [StringArgument()]

    def run(self):
        pass
