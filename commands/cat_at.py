from base.option import StringOption
from base.command import BaseCommand
from base.arguments import IntArgument, StringArgument
from db.dao.file_dao import FileDao
from db.dao.sector_dao import SectorDao
from db.base import SECTOR_SIZE
from math import ceil


class CatAtCommand(BaseCommand):
    """Without -w option, cat-at reads the content which starts at the
    specified index with a specific size (which is taken as a separate
    input).
    With the -w option, it appends the content that is logged
    by the user separately at the specified index.

    Usage: cat-at <index> <fileName>
    cat-at -w <index> <fileName>"""

    command = 'cat-at'
    arguments = [IntArgument(),  StringArgument()]
    options = [StringOption('-w')]

    aliases = ['cat_at', ]

    def write_to_file(self, file, index, text):
        file_size = FileDao.get_file_size(file)
        # If index is larger than the end of the file
        # Append data at the end of the file
        if index >= file_size:
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

            end_sectors.sort(key=lambda sector: sector.order)

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
                SectorDao.insert_sector_data(
                    sector, data=sector.data,
                    order=end_order, file_id=sector.file_id)

    def run(self, *args, **kwargs):
        index = self.arguments[0].data
        path = self.arguments[1].data
        file = self.context.parse(path, True)

        if self.options[0].exists:
            text = kwargs.get('text', None) or \
                   self.get_input('Start Writing: ', prefix=False)
            self.write_to_file(file, index, text)
        else:
            size = kwargs.get('size', None) or \
                   int(self.get_input('Total size to read:', prefix=False))
            content = FileDao.read_from_file(file, index, size)
            self.log(content, prefix=False)
