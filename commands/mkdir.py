from base.command import BaseCommand
from base.arguments import StringArgument

from db.models.directory import Directory
from db.dao.directory_dao import DirectoryDao


class MkDirCommand(BaseCommand):
    command = 'mkdir'
    arguments = [StringArgument()]

    def run(self):
        DirectoryDao.create_directory(directory=Directory(
            name=self.arguments[0].data,
            directory_id=self.context.current_directory.id
        ))
