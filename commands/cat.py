from base.option import StringOption
from base.command import BaseCommand
from base.arguments import StringArgument
from db.dao.file_dao import FileDao


class CatCommand(BaseCommand):
    """Prints the file to terminal. If '-w' option is specified, the cat command
    prompts the user for input and overwrites the file with that input.

    Usage: cat [OPTIONS] <path_to_file>
    """

    command = 'cat'
    arguments = [StringArgument()]
    options = [StringOption('-w')]

    def write_to_file(self, file, text):
        FileDao.remove_data_in_file(file)
        FileDao.insert_data_in_file(file, text)

    def run(self, *args, **kwargs):
        path = self.arguments[0].data
        file = self.context.parse(path, True)

        if self.options[0].exists:
            self.log('Warning: Data will be overwritten', prefix=False)
            text = kwargs.get('text', None) or self.get_input(
                'Start Writing: ', prefix=False)
            self.write_to_file(file, text)
        else:
            content = FileDao.read_from_file(file)
            self.log(content, prefix=False)
