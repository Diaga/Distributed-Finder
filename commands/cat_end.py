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

        if (FileDao.is_unique_filename(filename, current_directory)):
            self.log('InvalidEntry: File does not exist', prefix=False)
            # raise ValueError('File does not exist')
        else:
            file = FileDao.get_file(filename, current_directory)
            text = self.get_input('Start Writing: ', prefix=False)
            divs = [(text[i:i+sector_size()])
                    for i in range(0, len(text), sector_size())]
            for div in divs:
                if (SectorDao.is_memory_full()):
                    raise MemoryError(
                        'Memory is full! ' +
                        'All available sectors used up!')
                sector = SectorDao.get_first_unused_sector()
                SectorDao.insert_sector_data(
                    sector, div, True, file.id)

            # Debugging
            file_sectors = SectorDao.get_sectors_linked_to_file(file)
            self.log(
                f'The sectors of the file are {file_sectors}',
                prefix=False)
            print('The text in the file is:')
            for sector in file_sectors:
                print(sector.data, end='')
            print()

            """
            sector3 = Sector(
                data=bytes(json.dumps("st for fun"), 'utf8'),
                file_id=file.id
            )
            SectorDao.create_sector(sector3)
            """
