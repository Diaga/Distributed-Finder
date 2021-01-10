from base.connection import Client, message_builder, message_decompose, \
    Action, Status


def main():
    username = input('Please enter Distributed Finder '
                     'username(default: Guest): ')
    address = input(
        'Please enter Distributed Finder server address (default: localhost): '
    )

    with Client(username=username, address=address) as client:
        if client.status == Status.OK:
            while True:
                msg = client.recv()

                if client.status == Status.OK:
                    messages = message_decompose(msg)

                    for action, message in messages:
                        if action == Action.INPUT:
                            user_input = input(f'{client.username}@{message} ')
                            client.send(message_builder(
                                Action.INPUT, user_input
                            ))
                        elif action == Action.OUTPUT:
                            print(message)
                else:
                    print('Error receiving data from server: ', msg)
                    break

        else:
            print('Could not establish connection')


if __name__ == '__main__':
    main()
