from db.dao.sector_dao import SectorDao
from base.command import BaseCommand
from base.arguments import StringArgument
from db.base import sector_size
from db.dao.file_dao import FileDao


class CatEndCommand(BaseCommand):
    command = 'cat_end'
    arguments = [StringArgument()]

    def run(self):
        filename = self.arguments[0].data
        current_directory = self.context.current_directory

        if (FileDao.is_unique_filename(filename, current_directory)
                or not FileDao.is_valid_filename(filename)):
            raise ValueError('InvalidEntry: File does not exist')
        else:
            file = FileDao.get_file_from_current_directory(
                current_directory, filename)
            text = self.get_input('Start Writing: ', prefix=False)
            divs = []
            for cap in range(0, len(text), sector_size()):
                divs.append(text[cap: cap + sector_size()])

            order = FileDao.get_highest_order_of_sectors(file)
            for div in divs:
                if SectorDao.is_memory_full():
                    raise MemoryError(
                        'Memory is full! ' +
                        'All available sectors used up!')

                order += 1
                sector = SectorDao.get_first_unused_sector()
                SectorDao.insert_sector_data(
                    sector, div, order, True, file.id)
