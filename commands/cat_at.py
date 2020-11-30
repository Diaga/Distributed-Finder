from base.option import StringOption
from base.command import BaseCommand
from base.arguments import IntArgument, StringArgument
from db.dao.file_dao import FileDao
from db.dao.sector_dao import SectorDao
from db.base import SECTOR_SIZE
from math import ceil


class CatAtCommand(BaseCommand):
    command = 'cat-at'
    arguments = [IntArgument(), StringArgument()]
    options = [StringOption('-w')]

    def write_to_file(self, file, index, text):
        file_size = FileDao.get_file_size(file)
        # If index is larger than the end of the file
        # Append data at the end of the file
        if (index >= file_size):
            FileDao.insert_data_in_file(file, text)

        else:
            # The sector in which data is to be manipulated
            start_append_sector_order = ceil((index + 1) / SECTOR_SIZE)
            start_append_sector = [
                sector for sector in
                file.sectors if sector.order == start_append_sector_order][0]

            # The remaining sectors to be appended at the end
            end_sectors = [
                sector for sector in file.sectors
                if sector.order > start_append_sector_order
            ]

            # Taking the data out of the sector and
            # Concatenating with the provided input at the
            # specified index
            start_append_sector_data = start_append_sector.data
            start_index = index % SECTOR_SIZE
            text = start_append_sector_data[0:start_index] + \
                text + start_append_sector_data[start_index:]

            # Removing the sector data which was manipulated
            SectorDao.insert_sector_data(start_append_sector)

            # Inserting the provided data
            last_append_sector_order = FileDao.insert_data_in_file(
                file, text, start_append_sector_order - 1)

            # Reordering the previous sectors
            end_order = last_append_sector_order
            for sector in end_sectors:
                end_order += 1
                sector.order = end_order

    def read_from_file(self, file, index, size):
        file_size = FileDao.get_file_size(file)
        if (index >= file_size):
            raise ValueError(
                'Index larger than content in file!')
        # The sector from which data is to be read
        start_read_sector_order = ceil((index + 1) / SECTOR_SIZE)
        start_read_sector = [
            sector for sector in
            file.sectors if sector.order == start_read_sector_order][0]

        # The remaining sectors to be read
        end_sectors = [
            sector for sector in file.sectors
            if sector.order > start_read_sector_order
        ]
        # Sorting the remaining sectors by order
        end_sectors.sort(key=lambda sector: sector.order)

        # Read content of the sector from the specified index
        start_read_sector_data = start_read_sector.data
        start_index = index % SECTOR_SIZE
        content = start_read_sector_data[start_index:]

        # Read the content till the size specified
        count = 0
        while (size < len(content)) and (count < len(end_sectors)):
            content += end_sectors[count].data
            count += 1
        return content[:size]

    def run(self):
        index = self.arguments[0].data
        path = self.arguments[1].data
        file = self.context.parse(path, True)

        if self.options[0].exists:
            text = self.get_input('Start Writing: ', prefix=False)
            self.write_to_file(file, index, text)

        else:
            size = int(self.get_input('Total size to read:', prefix=False))
            content = self.read_from_file(file, index, size)
            self.log(content, prefix=False)
