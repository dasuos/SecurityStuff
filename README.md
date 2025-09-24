> ⚠️ **Educational use only / Pouze pro vzdělávací účely**  
>  
> This repository contains experimental and demonstrative code intended **only** for research and educational purposes. The code is **not** intended for malicious use or production deployment. Use at your own risk. The author assumes no responsibility for misuse.  
>  
> Tento repozitář obsahuje experimentální a demonstrativní kód určený **výhradně** pro výzkum a vzdělávání. Kód **není** určen k útokům ani k nasazení do produkce. Použití na vlastní riziko. Autor nenese odpovědnost za zneužití.
>

# SecurityStuff
Demonstration of security research and educational proofs-of-concept in Python and C

## ARP spoofing - arp_spoofing
**DO NOT RUN** on production networks or public infrastructure. Run **only** in an isolated disposable VM or a completely controlled lab network (host-only / virtual network) and with explicit consent from all participants.

**arp_spoofing_attack.py**
- Educational demo of ARP spoofing attack (for installing Scapy, use <code>pip3 install --pre scapy[basic]</code>)
**arp_spoofing_detection.py**
- Script demonstrating ARP spoofing detection by mapping MAC and IP addresses (for installing Scapy, use <code>pip3 install --pre scapy[basic]</code>)

## Ransomware - ransomware
**DO NOT RUN** on production or persistent hosts. Run only in an isolated disposable VM snapshot only for research/educational purposes

**ransomware.py**
- Educational demo that recursively iterates through a directory, encrypting all files with a symmetric key, which is then encrypted with a public key
- For generating RSA private and public key, use for example: <code>openssl genrsa -out rsa_private.key 4096</code> and <code>openssl rsa -in rsa_pair.key -pubout -out rsa_public.key</code>

**decryption.py**
- The decryption of the symmetric key with the private key, which is used to decrypt all files in a directory recursively

## Reverse shell - reverse_shell
**reverse_shell.py**
- Reverse shell connecting to CNC server, receiving, and executing commands
- To extend the reverse shell with a secure connection, see [TLS sockets](#tls-sockets---tls_sockets)

**cnc_server.py**
- CNC server accepting client connections, sending commands, and displaying output
- To extend the CNC server with a secure connection, see [TLS sockets](#tls-sockets---tls_sockets)

## Rootkit - rootkit
**DO NOT RUN** on production or persistent hosts. Run only in an isolated disposable VM snapshot only for research/educational purposes

**rootkit.c**
- Educational demo of simple rootkit blocking reboot system call by disabling write protect flag (cr0 register) and overwriting function pointer in the system call table
- By using a virtual machine, compile the kernel module by running <code>make</code> and <code>sudo insmod rootkit.ko</code>, then reboot to verify that the kernel has not shut down, and try to ping the machine

## TLS sockets - tls_sockets
- TLS sockets using elliptic-curve Diffie-Hellman key exchange
- Generate the server's private key and certificate by running: <code>openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout server.key -out server.crt</code>
- Generate the client’s private key and certificate by running: <code>openssl req -new -newkey rsa:3072 -days 365 -nodes -x509 -keyout client.key -out client.crt</code>

**tls_client.py**
- The client socket that establishes a secure connection to the server and sends the message from the input

**tls_server.py**
- The server socket that accepts a secure connection and receives the message from the client
