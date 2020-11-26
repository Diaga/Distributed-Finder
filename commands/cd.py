from base.command import BaseCommand
from base.arguments import StringArgument


class CDCommand(BaseCommand):

    command = 'cd'
    arguments = [StringArgument()]

    def run(self):
        path = self.arguments[0].data

        parsed_directory = self.context.parse_dir(path)
        self.context.current_directory = parsed_directory
