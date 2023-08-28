import socket
from sys import argv


def spoof(
    smtp_server_ip: str,
    port: int,
    from_address: str,
    to_address: str,
    content: str
) -> None:
    socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_instance.connect((smtp_server_ip, port))

    display_response(socket_instance)

    messages = [
        'HELO {:s}\n'.format(from_address.split('@')[1]),
        'MAIL FROM:<{:s}>\n'.format(from_address),
        'RCPT TO:<{:s}>\n'.format(to_address),
        'DATA\n',
        '{:s}\r\n.\r\n'.format(content),
        'QUIT\n',
    ]
    for message in messages:
        send_message(socket_instance, message)
        display_response(socket_instance)

    socket_instance.close()


def send_message(socket_instance: socket.socket, message: str):
    print(message)
    socket_instance.send(message.encode())


def display_response(socket_instance: socket.socket) -> None:
    print(socket_instance.recv(1024).decode())


smtp_server_ip = argv[1]
port = argv[2]
from_address = argv[3]
to_address = argv[4]
content = argv[5]

spoof(smtp_server_ip, int(port), from_address, to_address, content)
