from base.command import BaseCommand
from base.arguments import StringArgument

from db.models.file import File
from db.dao.file_dao import FileDao


class TouchCommand(BaseCommand):
    command = 'touch'
    arguments = [StringArgument()]

    def run(self):
        filename = self.arguments[0].data
        current_directory = self.context.current_directory

        if FileDao.is_valid_filename(filename):
            if FileDao.is_unique_filename(filename, current_directory):
                file = File(
                    name=filename,
                    directory_id=current_directory.id
                )
                FileDao.create_file(file)
            else:
                raise ValueError('File already exists')
        else:
            raise ValueError('file name should not start with ' +
                             'a special character and should not' +
                             ' contain \\ / characters')
