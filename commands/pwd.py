from db.dao.file_dao import FileDao
from base.command import BaseCommand


class PWDcommand(BaseCommand):

    command = 'pwd'

    def run(self):
        path = FileDao.get_path(self)
        self.log(path)
