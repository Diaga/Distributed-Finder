from base.command import BaseCommand
from base.arguments import StringArgument
from db.dao.file_dao import FileDao


class CatEndCommand(BaseCommand):
    """Appends user input at the end of the given file name.

        Usage: cat-end <filename>

        this command prompts the user to input the text,
        by displaying "Start Writing: ". Whatever is entered
        is appended to the <filename>."""

    command = 'cat-end'
    arguments = [StringArgument()]

    def run(self, *args, **kwargs):
        path = self.arguments[0].data
        file = self.context.parse(path, True)
        text = next(iter(args), None) or self.get_input(
            'Start Writing: ', prefix=False)
        FileDao.insert_data_in_file(file, text)
