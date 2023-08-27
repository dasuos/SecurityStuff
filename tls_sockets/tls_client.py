import socket
import ssl

client_key = 'client.key'
client_certificate = 'client.crt'
server_certificate = 'server.crt'

port = 443
hostname = '127.0.0.1'

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT, cafile=server_certificate)
context.check_hostname = False

context.load_cert_chain(certfile=client_certificate, keyfile=client_key)
context.load_verify_locations(cafile=server_certificate)

# use elliptic-curve Diffie-Hellman and TLS version 1.3 only
context.options |= ssl.OP_SINGLE_ECDH_USE
context.minimum_version = ssl.TLSVersion.TLSv1_3
context.maximum_version = ssl.TLSVersion.TLSv1_3

with socket.create_connection((hostname, port)) as socket_instance:
    # wrap the socket and encrypt the data sent
    with context.wrap_socket(
        socket_instance,
        server_side=False,
        server_hostname=hostname
    ) as wrapped_socket_instance:
        while (message := input('Enter the message: ')) != 'exit':
            wrapped_socket_instance.send(message.encode())

            server_response = wrapped_socket_instance.recv(1024).decode()
            print('Server response: {:s}'.format(server_response))
