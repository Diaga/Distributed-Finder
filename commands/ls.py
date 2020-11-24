from base.command import BaseCommand

from db.dao.directory_dao import DirectoryDao


class LSCommand(BaseCommand):
    command = 'ls'

    def run(self):
        self.log(DirectoryDao.get_directories_from_current_directory(
            self.context.current_directory), prefix=False
        )
