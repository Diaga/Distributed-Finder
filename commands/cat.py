from base.command import BaseCommand
from base.arguments import StringArgument
from db.dao.file_dao import FileDao


class CatCommand(BaseCommand):
    command = 'cat'
    arguments = [StringArgument()]

    def run(self):
        path = self.arguments[0].data
        file = self.context.parse(path, True)
        self.log('WARNING: Data will be overwritten', prefix=False)
        FileDao.remove_data_in_file(file)
        text = self.get_input('Start Writing: ', prefix=False)
        FileDao.insert_data_in_file(file, text)
