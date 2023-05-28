from socket import *

server_port = 8000

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(('', server_port))
server_socket.listen(1)

print('Listening for connections')

connection_socket, address = server_socket.accept()

print('Connecting ' + str(address))

message = connection_socket.recv(1024)
print(message)

command = ''
while command != 'exit':
    command = input('Enter a command:')
    connection_socket.send(command.encode())
    message = connection_socket.recv(1024).decode()
    print(message)

connection_socket.shutdown(SHUT_RDWR)
connection_socket.close()
