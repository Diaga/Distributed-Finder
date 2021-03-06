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
            try:
                while True:
                    msg = client.recv()

                    if client.status == Status.OK:
                        messages = message_decompose(msg)

                        for action, message in messages:
                            if action == Action.INPUT:
                                prompt = f'{client.username}@{message} ' \
                                    if message else ''
                                user_input = input(prompt)
                                client.send(message_builder(
                                    Action.INPUT, user_input
                                ))
                            elif action == Action.OUTPUT:
                                print(message)
                    else:
                        print('Error receiving data from server: ', msg)
                        break
            except KeyboardInterrupt:
                print('\nExiting client after cleaning up...')

        else:
            print('Could not establish connection')


if __name__ == '__main__':
    main()
