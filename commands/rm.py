from base.command import BaseCommand
from base.arguments import StringArgument


class RmCommand(BaseCommand):

    command = 'rm'

    arguments = [StringArgument(required=False)]
