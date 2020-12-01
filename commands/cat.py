from base.option import StringOption
from base.command import BaseCommand
from base.arguments import StringArgument
from db.dao.file_dao import FileDao


class CatCommand(BaseCommand):
    command = 'cat'
    arguments = [StringArgument()]
    options = [StringOption('-w')]

    def read_From_file(self, file):
        if file.is_empty:
            raise ValueError('File is empty! No contents to show')
        file_sectors = file.sectors
        file_sectors.sort(key=lambda sector: sector.order)
        content = ''
        for sector in file_sectors:
            content += sector.data
        return content

    def write_to_file(self, file, text):
        FileDao.remove_data_in_file(file)
        FileDao.insert_data_in_file(file, text)

    def run(self):
        path = self.arguments[0].data
        file = self.context.parse(path, True)

        if self.options[0].exists:
            self.log('Warning: Data will be overwritten', prefix=False)
            text = self.get_input('Start Writing: ', prefix=False)
            self.write_to_file(file, text)
        else:
            content = self.read_From_file(file)
            self.log(content, prefix=False)
