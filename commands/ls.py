from base.command import BaseCommand

from db.dao.directory_dao import DirectoryDao
from db.dao.file_dao import FileDao


class LSCommand(BaseCommand):
    command = 'ls'

    def run(self):
        def display_lists(dir_list):
            list_dirlist = list(dir_list)
            for i in range((len(list_dirlist)) - 1):
                list_dirlist[i] = str(list_dirlist[i])
            for i in range((len(list_dirlist)) - 1):
                list_dirlist[i] += '       '
            n = m = 0
            while m < len(list_dirlist):
                m = m+3
                if ((len(list_dirlist)-1) >= (n+2)):
                    print(list_dirlist[n], list_dirlist[n+1],
                          list_dirlist[n+2])
                elif((len(list_dirlist)-1) < (n+2) 
                    and (len(list_dirlist)-1) >= (n+1)):
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
