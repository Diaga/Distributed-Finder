from base.command import BaseCommand

from db.dao.directory_dao import DirectoryDao
from db.dao.file_dao import FileDao


class LSCommand(BaseCommand):
    """Print out the files and directories that presently
        exist in the directory user currently resides in.

        Usage: ls"""

    command = 'ls'

    def display_lists(self, list_dirlist):
        """
        :param list_dirlist: List of directory model objects

        .. versionchanged: Lab 10: Change argument from dir_list to
        _dir_list to avoid shadowing and simplify conditionals
        """
        for i in range((len(list_dirlist)) - 1):
            list_dirlist[i] = str(list_dirlist[i])
        for i in range((len(list_dirlist)) - 1):
            list_dirlist[i] += '       '
        n = m = 0
        x = len(list_dirlist)
        while m < x:
            m = m + 3
            if (x - 1) >= (n + 2):
                self.log(f'{list_dirlist[n]} '
                         f'{list_dirlist[n + 1]} '
                         f'{list_dirlist[n + 2]}', prefix=False)
            elif (n + 2) > (x - 1) >= (n + 1):
                self.log(f'{list_dirlist[n]} {list_dirlist[n + 1]}',
                         prefix=False)
            else:
                self.log(f'{list_dirlist[n]}', prefix=False)
            n = m

    def run(self):

        dir_list = DirectoryDao.get_directories_from_current_directory(
            self.context.current_directory)
        file_list = FileDao.get_files_from_current_directory(
            self.context.current_directory)
        self.log('Directories: ', prefix=False)
        self.display_lists(dir_list)
        self.log('Files: ', prefix=False)
        self.display_lists(file_list)
