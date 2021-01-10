import sys
import socket

from main import DEFAULT_COMMANDS
from base.terminal import BaseTerminal
from base.connection import Server, ClientConnection, Status, \
    message_builder, message_decompose, Action


class ServerTerminal(BaseTerminal):

    def __init__(self, connection, commands=None, prefix='finder'):
        self.connection = connection
        super().__init__(commands=commands, prefix=prefix)

    def log(self, message, prefix=True, stdout=None):
        if prefix:
            message = f'{self.get_prefix} {message}'

        try:
            self.connection.send(
                message_builder(Action.OUTPUT, message)
            )
        except socket.error as e:
            print(e)

    def get_input(self, prompt=None, prefix=True):
        if prompt is not None:
            self.log(prompt, prefix=prefix)

        message = ''
        if prefix:
            message = self.get_prefix

        try:
            self.connection.send(
                message_builder(Action.INPUT, message)
            )
        except socket.error as e:
            print(e)


def client_handler(conn, address):
    """Handle individual client connection"""
    with ClientConnection(conn) as client_connection:
        terminal = ServerTerminal(
            client_connection,
            commands=DEFAULT_COMMANDS,
        )

        while True:
            terminal.get_input()
            message = client_connection.recv()

            if client_connection.status == Status.OK:
                messages = message_decompose(message)

                for action, user_input in messages:
                    if action == Action.INPUT:
                        command, arguments, found, _ = terminal.match_command(
                            user_input
                        )
                        terminal.sansio_run(
                            command, arguments, found
                        )
            else:
                print(f'Error receiving data from client: {address}')
                break


def main():

    host = sys.argv[1] if len(sys.argv) == 2 else None

    with Server(host) as server:
        if server.status == Status.OK:
            while True:
                conn, address = server.accept()

                if server.status == Status.OK:
                    server.hand_off(conn, address, client_handler)
                else:
                    print('Error accepting new connection')
                    break
        else:
            print('Could not bind server')


if __name__ == '__main__':
    main()
