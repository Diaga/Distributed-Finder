import socket
import json
from threading import Thread
import threading

BUFF = 1024
PORT = 95
ACTIVE_CONNECTIONS_POOL = []
THREADS = []


def client_thread(client_connection, client_address):
    user_id = None
    thread_id = threading.get_ident()
    while True:
        data = json.loads(client_connection.recv(
            BUFF).decode().replace("\'", "\""))
        if not data:
            break
        # AUTH ACTION
        if data['action'] == 'AUTH':
            user_id = data['payload']['user_id'] + str(thread_id)
            ACTIVE_CONNECTIONS_POOL.append(user_id)
            print('Connection:', str(client_address), 'UserID:', user_id)
            client_connection.send(
                str(
                    {'action': 'AUTH', 'payload': {'user_id': user_id}}
                    ).encode())
            client_connection.send(
                str(
                    {'action': 'INPUT', 'payload': {'message': 'prefix: '}}
                    ).encode())
        # INPUT ACTION
        elif data['action'] == 'INPUT' and user_id is not None:
            user_input = data['payload']['message']
            if user_input == 'exit':
                break
            output = 'output: did something with input:'+user_input
            client_connection.send(
                str(
                    {'action': 'OUTPUT', 'payload': {'message': output}}
                    ).encode())
        # OUTPUT ACTION
        elif data['action'] == 'OUTPUT' and user_id is not None:
            client_connection.send(
                str(
                    {'action': 'INPUT', 'payload': {'message': 'prefix: '}}
                    ).encode())

    print('Closing Connection: ', str(client_address), 'UserID:', user_id)
    client_connection.close()
    if user_id is not None:
        ACTIVE_CONNECTIONS_POOL.remove(user_id)


def run_server_thread(socket_):
    while(input() != 'exit'):
        continue
    socket_.close()


def server():
    host = socket.gethostname()
    socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        socket_.bind((host, PORT))
    except socket.error as e:
        print('Error binding socket:', e)

    socket_.listen()
    Thread(target=run_server_thread, args=[socket_]).start()
    print("Server is listening... (type 'exit' to close)")
    while True:
        try:
            conn, address = socket_.accept()
        except socket.error:
            print(
                'Closing server after all client connections are closed...'
                )
            break
        thread_ = Thread(target=client_thread, args=[conn, address])
        thread_.start()
        THREADS.append(thread_)

    for thread in THREADS:
        thread.join()


if __name__ == '__main__':
    server()
