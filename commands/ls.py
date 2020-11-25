from base.command import BaseCommand

from db.dao.directory_dao import DirectoryDao
from db.dao.file_dao import FileDao


class LSCommand(BaseCommand):
    command = 'ls'

    def run(self):
        self.log(DirectoryDao.get_directories_from_current_directory(
            self.context.current_directory), prefix=False
        )
        # logging files - temp
        self.log(FileDao.get_files_from_current_directory(
            self.context.current_directory), prefix=False)
