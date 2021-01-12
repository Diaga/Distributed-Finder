import socket
import json
import threading
from enum import Enum, auto


PORT = 9000
BUFF_SIZE = 1024


def message_encode(message):
    """Encodes json message to be sent to server

    :param: message: Message to encode"""
    return str(f'{message}|').encode()


def message_decode(messages):
    """Decodes message received from server back to json

    :param: message: Message to decode"""
    return [json.loads(message) for message in
            messages.decode().replace('\'', '\"').split('|')[:-1]]


def message_builder(action, message=None):
    """Builds message to send

    :param: action: Protocol action
    :param: message: Protocol message"""
    msg = {
        'action': action, 'payload': {}
    }

    if message is not None:
        msg['payload']['message'] = message

    return msg


def message_decompose(messages):
    """Decomposes message to a tuple of action, message"""
    return [(message.get('action'),
             message['payload'].get('message')) for message in messages]


class Status(Enum):

    UNSET = auto()
    OK = auto()
    ERROR = auto()


class Action:

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'


class Client:

    def __init__(self, username=None, address=None):
        self.address = address or socket.gethostname()
        self.username = username or 'Guest'

        self.connection = None
        self.status = Status.UNSET

    def connect(self):
        """Connects to Distributed Finder server at specified address"""
        try:
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.connection.connect((self.address, PORT))
        except (socket.error, socket.gaierror) as e:
            self.status = Status.ERROR
            return e

        self.status = Status.OK

    def send(self, message):
        """Send message to server

        :param: message: Message to send"""
        try:
            self.connection.send(message_encode(message))
        except socket.error as e:
            self.status = Status.ERROR
            return e

        self.status = Status.OK

    def recv(self):
        """Receive message from server"""
        try:
            message = self.connection.recv(BUFF_SIZE)
        except socket.error as e:
            self.status = Status.ERROR
            return e

        return message_decode(message)

    def close(self):
        """Close the connection from server"""
        self.connection.close()

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class Server:

    def __init__(self, host=None):
        self.host = host or socket.gethostname()
        self.status = Status.UNSET

        self.connection = None
        self.threads = []

    def serve(self):
        """Binds the port and starts listening"""
        try:
            self.connection = socket.socket(socket.AF_INET,
                                            socket.SOCK_STREAM)
            self.connection.bind((self.host, PORT))
            self.connection.listen()
        except socket.error as e:
            self.status = Status.ERROR
            return e

        self.status = Status.OK

    def accept(self):
        """Accepts a new connection"""
        try:
            conn, address = self.connection.accept()
        except socket.error as e:
            self.status = Status.ERROR
            return e

        return conn, address

    def hand_off(self, conn, address, handler):
        """Performs hand off to a new thread"""
        thread = threading.Thread(
            target=handler, args=[conn, address]
        )
        thread.start()
        self.threads.append(thread)

    def __enter__(self):
        self.serve()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for thread in self.threads:
            thread.join()

        self.connection.close()


class ClientConnection:

    def __init__(self, connection):
        self.connection = connection
        self.status = Status.UNSET

    def send(self, message):
        """Send message to client

        :param: message: Message to send"""
        try:
            self.connection.send(message_encode(message))
        except socket.error as e:
            self.status = Status.ERROR
            return e

        self.status = Status.OK

    def recv(self):
        """Receive message from client"""
        try:
            message = self.connection.recv(BUFF_SIZE)
        except socket.error as e:
            self.status = Status.ERROR
            return e

        return message_decode(message)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
