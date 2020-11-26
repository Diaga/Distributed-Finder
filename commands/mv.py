from base.command import BaseCommand
from base.arguments import StringArgument

from db.db import DB


class MvCommand(BaseCommand):

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

        to_be_moved.directory_id = target_dir.id
        DB().session.commit()
