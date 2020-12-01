from base.command import BaseCommand
from base.arguments import StringArgument


class CDCommand(BaseCommand):
    """Used to change the directory in which the user resides in,
        to one of the constituents directories.
        
        Usage: cd <directory_name>"""

    command = 'cd'
    arguments = [StringArgument()]

    def run(self):
        path = self.arguments[0].data

        parsed_directory = self.context.parse(path)
        self.context.current_directory = parsed_directory
