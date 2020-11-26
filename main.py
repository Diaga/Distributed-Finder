import os

from base.terminal import BaseTerminal

from commands.ping import PingCommand
from commands.cd import CDCommand
from commands.ls import LSCommand
from commands.mkdir import MkDirCommand
from commands.touch import TouchCommand

from db.db import DB


def main():
    """Start Finder Terminal and create connection to DB"""
    db = DB()
    db.connect(os.path.join(os.getcwd(), 'finder.db'))

    terminal = BaseTerminal(commands=[
        PingCommand, CDCommand, MkDirCommand, LSCommand, TouchCommand
    ])
    terminal.run()


if __name__ == '__main__':
    main()
