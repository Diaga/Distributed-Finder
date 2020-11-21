from base.terminal import BaseTerminal
from commands.ping.command import PingCommand


def main():
    """Start Finder Terminal"""
    terminal = BaseTerminal(commands=[PingCommand()])
    terminal.run(welcome_message='Last login at X')


if __name__ == '__main__':
    main()
