from db.dao.file_dao import FileDao
from base.command import BaseCommand


class FMapCommand(BaseCommand):
    """Displays the whole memory map. Outputting the details
        of all files existing on the system.

        Usage: fmap """
        
    command = 'fmap'

    def run(self):
        files = FileDao.get_all_files()
        if (len(files) != 0):
            format_string = '{:<38} {:<7} {:<23} {:<40} {:<8}'
            # Printing the header
            self.log('', prefix=False)
            self.log(format_string.format(
                'MemoryAddress', 'Bytes', 'Path',
                'Sector Memory Address', 'Sector Order'), prefix=False)
            self.log('', prefix=False)

            # Printing memory specs for all files
            for file in files:
                path = FileDao.get_path(file)
                sectors = file.sectors
                map = format_string.format(
                    file.id, FileDao.get_file_size(file),
                    path, '' if file.is_empty else sectors[0].id,
                    '' if file.is_empty else sectors[0].order)
                self.log(map, prefix=False)
                for sector in sectors:
                    if sector == sectors[0]:
                        continue
                    self.log(format_string.format(
                        '', '', '', str(sector.id), str(sector.order)),
                        prefix=False)
            self.log('', prefix=False)
        else:
            self.log('Memory is Empty!', prefix=False)
