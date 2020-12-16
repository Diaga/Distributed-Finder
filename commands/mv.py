from base.command import BaseCommand
from base.arguments import StringArgument

from db.db import DB


class MvCommand(BaseCommand):
    """Moves the given file or directory to the given target directory.
        Raises an error if the file/directory to be moved does not exist.

        Usage: mv <filename1> <targetDirectory>

        above command moves filename1 (either a file or a directory)
        to the targetDirectory."""

    command = 'mv'
    arguments = [StringArgument(), StringArgument()]

    def run(self):
        try:
            to_be_moved = self.context.parse(
                self.arguments[0].data, is_file=True
            )
        except ValueError:
            try:
                to_be_moved = self.context.parse(self.arguments[0].data)
            except ValueError:
                raise ValueError('Source does not exists!')

        target_dir = self.context.parse(self.arguments[1].data)

        if self.arguments[0].data == self.arguments[1].data:
            raise ValueError('You cannot move source to the same target')

        to_be_moved.directory_id = target_dir.id
        DB().session.commit()
