import os

from base.terminal import BaseTerminal

from commands.ping import PingCommand
from commands.cd import CDCommand
from commands.ls import LSCommand
from commands.mkdir import MkDirCommand
from commands.touch import TouchCommand
from commands.cat_end import CatEndCommand
from commands.rm import RmCommand
from commands.mv import MvCommand
from commands.pwd import PWDcommand

from db.db import DB


def main():
    """Start Finder Terminal and create connection to DB"""
    db = DB()
    db.connect(os.path.join(os.getcwd(), 'finder.db'))

    terminal = BaseTerminal(commands=[
        PingCommand, CDCommand, MkDirCommand, LSCommand,
        TouchCommand, CatEndCommand, RmCommand, MvCommand, PWDcommand
    ])
    terminal.run()


if __name__ == '__main__':
    main()
