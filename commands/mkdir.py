from base.command import BaseCommand
from base.arguments import StringArgument

from db.models.directory import Directory
from db.dao.directory_dao import DirectoryDao


class MkDirCommand(BaseCommand):
    """Used to make a new directory inside the directory
        user presently exists in.

        Usage: mkdir dir_1"""

    command = 'mkdir'
    arguments = [StringArgument()]

    def run(self):
        dirname = self.arguments[0].data
        current_directory = self.context.current_directory
        if DirectoryDao.is_valid_dirname(dirname):
            if DirectoryDao.is_unique_direname(dirname, current_directory):
                directory = Directory(
                    name=dirname,
                    directory_id=current_directory.id
                )
                DirectoryDao.create_directory(directory)
            else:
                raise ValueError('Directory already exists')
        else:
            raise ValueError('Directory name should not start with ' +
                             'a special character and should not' +
                             ' contain \\ / . characters')
