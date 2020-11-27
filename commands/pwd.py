from base.command import BaseCommand
from db.dao.directory_dao import DirectoryDao


class PWDcommand(BaseCommand):

    command='pwd'
    def run(self):
        current = str(self.context.current_directory)
        path = '/'+current
        root = DirectoryDao.get_root_directory()
        restore = self.context.current_directory

        while (self.context.current_directory != root):
            
            parent = self.context.current_directory.directory
            str_parent = str(parent)
            path = '/'+str_parent+path
            self.context.current_directory = parent
        self.context.current_directory = restore
        self.log(path)

       
    
    
    