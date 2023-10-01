## TLS sockets - tls_sockets
- TLS sockets using elliptic-curve Diffie-Hellman key exchange
- Generate the server's private key and certificate by running: <code>openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout server.key -out server.crt</code>
- Generate the client’s private key and certificate by running: <code>openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout client.key -out client.crt</code>

**tls_client.py**
- The client socket that establishes a secure connection to the server and sends the message from the input

**tls_server.py**
- The server socket that accepts a secure connection and receives the message from the client
