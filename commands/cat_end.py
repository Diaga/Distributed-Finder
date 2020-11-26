from base.command import BaseCommand
from base.arguments import StringArgument
from db.dao.file_dao import FileDao


class CatEndCommand(BaseCommand):
    command = 'cat_end'
    arguments = [StringArgument()]

    def run(self):
        path = self.arguments[0].data
        file = self.context.parse(path, True)
        current_directory = self.context.current_directory

        if (FileDao.is_unique_filename(file.name, current_directory)
                or not FileDao.is_valid_filename(file.name)):
            raise ValueError('InvalidEntry: File does not exist')
        else:
            text = self.get_input('Start Writing: ', prefix=False)
            FileDao.insert_data_in_file(file, text)
