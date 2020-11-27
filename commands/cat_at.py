from base.command import BaseCommand
from base.arguments import IntArgument, StringArgument
from db.dao.file_dao import FileDao
from db.dao.sector_dao import SectorDao
from db.base import sector_size
from math import ceil


class CatAtCommand(BaseCommand):
    command = 'cat-at'
    arguments = [IntArgument(), StringArgument()]

    def run(self):
        index = self.arguments[0].data
        path = self.arguments[1].data
        file = self.context.parse(path, True)

        file_size = FileDao.get_file_size(file)
        text = self.get_input('Start Writing: ', prefix=False)
        # If index is larger than the end of the file
        # Append data at the end of the file
        if (index >= file_size):
            FileDao.insert_data_in_file(file, text)

        else:
            # The sector in which data is to be manipulated
            start_append_sector_order = ceil((index + 1) / sector_size())
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
            start_index = index % sector_size()
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
