import os

from base.terminal import BaseTerminal

from commands.ping import PingCommand
from commands.cd import CDCommand
from commands.ls import LSCommand
from commands.mkdir import MkDirCommand
from commands.touch import TouchCommand
from commands.cat_end import CatEndCommand
from commands.cat import CatCommand
from commands.cat_at import CatAtCommand
from commands.rm import RmCommand
from commands.mv import MvCommand
from commands.pwd import PWDcommand
from commands.fmap import FMapCommand
from commands.hello import HelloCommand
from commands.kthreads import KThreadsCommand

from db.db import DB


def main():
    """Start Finder Terminal and create connection to DB"""
    db = DB()
    db.connect(os.path.join(os.getcwd(), 'finder.db'))

    terminal = BaseTerminal(commands=[
        PingCommand, CDCommand, MkDirCommand, LSCommand, PWDcommand,
        TouchCommand, CatEndCommand, CatCommand, FMapCommand,
        CatAtCommand, RmCommand, MvCommand, HelloCommand, KThreadsCommand])
    terminal.run()


if __name__ == '__main__':
    main()
