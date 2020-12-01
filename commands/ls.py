from base.command import BaseCommand

from db.dao.directory_dao import DirectoryDao
from db.dao.file_dao import FileDao


class LSCommand(BaseCommand):
    """Print out the files and directories that presently
        exist in the directory user currently resides in.

        Usage: ls"""

    command = 'ls'

    def run(self):
        def display_lists(dir_list):
            list_dirlist = list(dir_list)
            for i in range((len(list_dirlist)) - 1):
                list_dirlist[i] = str(list_dirlist[i])
            for i in range((len(list_dirlist)) - 1):
                list_dirlist[i] += '       '
            n = m = 0
            x = len(list_dirlist)
            while m < x:
                m = m+3
                if ((x-1) >= (n+2)):
                    print(list_dirlist[n], list_dirlist[n+1],
                          list_dirlist[n+2])
                elif((x-1) < (n+2) and (x-1) >= (n+1)):
                    print(list_dirlist[n], list_dirlist[n+1])
                else:
                    print(list_dirlist[n])
                n = m
        dir_list = DirectoryDao.get_directories_from_current_directory(
                self.context.current_directory)
        file_list = FileDao.get_files_from_current_directory(
            self.context.current_directory)
        self.log('Directories: ')
        display_lists(dir_list)
        self.log('Files: ', prefix=False)
        display_lists(file_list)
