from base.command import BaseCommand
from base.arguments import StringArgument
from base.option import StringOption

from db.dao.directory_dao import DirectoryDao
from db.dao.file_dao import FileDao
from db.db import DB


class RmCommand(BaseCommand):
    """Used to delete files and directories. 
        Simple 'rm' with a filename will remove that file.
        Simple 'rm' with a directory name will raise an error.
        If '-rf' option specified, it will delete the desired
        directory along with all its constituent directories.

        Usage: rm <file_name>
        rm -rf <directory_name>"""


    command = 'rm'
    arguments = [StringArgument()]
    options = [StringOption('-rf')]

    def recursive_remove(self, directory):
        """Recursively removes directories
        :param directory: Directory model object to search"""
        directories = DirectoryDao.\
            get_directories_from_current_directory(directory)
        for directory in directories:
            self.recursive_remove(directory)
            DirectoryDao.delete_directory(directory, commit=False)

        files = FileDao.get_files_from_current_directory(directory)
        for file in files:
            FileDao.delete_file(file, commit=False)

        DirectoryDao.delete_directory(directory, commit=False)

    def run(self):
        if self.options[0].exists:
            directory = self.context.parse(self.arguments[0].data)

            self.recursive_remove(directory)
            DB().session.commit()
        else:
            file = self.context.parse(self.arguments[0].data, is_file=True)
            FileDao.delete_file(file)
