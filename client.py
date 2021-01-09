import socket
import sys
import json

PORT = 95
BUFF = 1024


def main():
    username = input('Please enter Distributed Finder username: ')
    server_address = input(
        'Please enter Distributed Finder server address (default: localhost):')
    print("type 'exit' when you are done...")
    if server_address or server_address != '':
        host = server_address
    else:
        host = socket.gethostname()
    try:
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Error creating socket:', e)
        sys.exit(0)
    try:
        socket_.connect((host, PORT))
    except socket.gaierror as e:
        print('Address Related Error connecting to server:', e)
    except socket.error as e:
        print('Connection Error:', e)
    # sending username to server
    try:
        socket_.send(
            str({'action': 'AUTH', 'payload': {'user_id': username}}).encode())
    except socket.error as e:
        print('Error sending username:', e)
    user_id = ''
    while True:
        try:
            data = json.loads(
                socket_.recv(BUFF).decode().replace("\'", "\""))
            if data['action'] == 'INPUT':
                user_input = input(data['payload']['message'])
                socket_.send(str(
                    {'action': 'INPUT', 'payload': {
                        'message': user_input, 'user_id': user_id}}
                )
                    .encode())
                if(user_input == 'exit'):
                    break
            elif data['action'] == 'OUTPUT':
                print(data['payload']['message'])
                socket_.send(str({
                    'action': 'OUTPUT', 'payload': {
                        'message': '', 'user_id': user_id}}
                ).encode())
            elif data['action'] == 'AUTH':
                user_id = data['payload']['user_id']
        except socket.error as e:
            print('Error sending or receiving data:', e)
    socket_.close()


if __name__ == '__main__':
    main()
