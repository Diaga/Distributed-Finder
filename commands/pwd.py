from db.dao.file_dao import FileDao
from base.command import BaseCommand


class PWDcommand(BaseCommand):
    """Returns the location of the present working directory,
        user current;y is residing in the file management system."""
    command = 'pwd'

    def run(self):
        path = FileDao.get_path(self)
        self.log(path)
