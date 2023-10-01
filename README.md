# SecurityStuff
Demonstration of security-related scripts with an educational purpose using Python and C

## ARP spoofing - arp_spoofing
**arp_spoofing_attack.py**
- Example of ARP spoofing attack (for installing Scapy, use <code>pip3 install --pre scapy[basic]</code>)

**arp_spoofing_detection.py**
- Script demonstrating ARP spoofing detection by mapping MAC and IP addresses (for installing Scapy, use <code>pip3 install --pre scapy[basic]</code>)

## Reverse shell - reverse_shell
**reverse_shell.py**
- Reverse shell connecting to CNC server, receiving, and executing commands
- To extend the reverse shell with secure connection, see [TLS sockets](#tls-sockets---tls_sockets)

**cnc_server.py**
- CNC server accepting client connections, sending commands, and displaying output
- To extend the CNC server with secure connection, see [TLS sockets](#tls-sockets---tls_sockets)

## Ransomware - ransomware
**ransomware.py**
- Ransomware recursively iterating through a directory encrypting all files with a symmetric key, which is after encrypted with a public key
- For generating RSA private and public key, use for example: <code>openssl genrsa -out rsa_private.key 4096</code> and <code>openssl rsa -in rsa_pair.key -pubout -out rsa_public.key</code>
- Use at your own risk

**decryption.py**
- The decryption of symmetric key with private key, which is after that used to recursively decrypt all files in a directory

## TLS sockets - tls_sockets
- TLS sockets using elliptic-curve Diffie-Hellman key exchange
- Generate the server's private key and certificate by running: <code>openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout server.key -out server.crt</code>
- Generate the client’s private key and certificate by running: <code>openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout client.key -out client.crt</code>

**tls_client.py**
- The client socket that establishes a secure connection to the server and sends the message from the input

**tls_server.py**
- The server socket that accepts a secure connection and receives the message from the client

## Rootkit - rootkit
**rootkit.py**
- Rootkit blocking reboot system call by disabling write protect flag (cr0 register) and overwriting function pointer in the system call table
- By using a virtual machine, compile the kernel module by running <code>make</code> and <code>sudo insmod rootkit.ko</code>, then reboot to verify that the kernel has not shut down and try to ping the machine
