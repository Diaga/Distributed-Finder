import tkinter as tk
from tkinter import filedialog

from functools import partial
from pathlib import Path
from os import path
from threading import Thread

from base.command import BaseCommand


class KThreadsCommand(BaseCommand):
    """Prompts for a file dialog to select files with appropriate
    commands and runs them with k threads.

        Usage: kthreads"""

    command = 'kthreads'

    def thread_run(self, input_file, output_file):

        with open(output_file, 'w') as out_f:
            with open(input_file, 'r') as in_f:
                for line in in_f.readlines():
                    command, arguments, found = self.context.\
                        terminal.match_command(line)
                    if found:
                        command.log = partial(self.log, stdout=out_f)

                        try:
                            command.validate(arguments)
                            command.run()
                        except (ValueError, MemoryError) as e:
                            command.log(e, prefix=False)
                        finally:
                            command.reset()
                    else:
                        command.log(f'terminal: command not found:'
                                    f' {command}', prefix=False)

    def run(self):
        root = tk.Tk()
        root.withdraw()

        file_path_list = filedialog.askopenfilenames(
            title='Select k files to run in k threads',
            filetypes=[('Text files', '.txt')]
        )

        threads = []

        for file_path in file_path_list:
            file_path = Path(file_path)

            output_file_path = path.join(
                file_path.parent,
                file_path.name.replace('input', 'output')
            )

            threads.append(Thread(target=self.thread_run,
                                  args=[file_path, output_file_path]))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()
