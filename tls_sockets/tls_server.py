import socket
import ssl

server_key = 'server.key'
server_certificate = 'server.crt'
client_certificate = 'client.crt'

port = 8080

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.verify_mode = ssl.CERT_REQUIRED

context.load_verify_locations(cafile=client_certificate)
context.load_cert_chain(certfile=server_certificate, keyfile=server_key)

# use elliptic-curve Diffie-Hellman and TLS version 1.3 only
context.options |= ssl.OP_SINGLE_ECDH_USE
context.minimum_version = ssl.TLSVersion.TLSv1_3
context.maximum_version = ssl.TLSVersion.TLSv1_3

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as socket_instance:
    socket_instance.bind(('', port))
    socket_instance.listen(1)

    # wrap the socket and encrypt the data sent
    with context.wrap_socket(
        socket_instance,
        server_side=True
    ) as wrapped_socket_instance:
        connection, address = wrapped_socket_instance.accept()
        print('Connection from {:s} established'.format(address[0]))

        while True:
            message = connection.recv(1024).decode()
            connection.send("Message '{:s}' received".format(message).encode())
