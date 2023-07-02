# SecurityStuff
Demonstration of security-related scripts using Python and C

## ARP spoofing - arp_spoofing
**arp_spoofing_attack.py**
- Example of ARP spoofing attack (for installing Scapy, use <code>pip3 install --pre scapy[basic]</code>)

**arp_spoofing_detection.py**
- Script demonstrating ARP spoofing detection by mapping MAC and IP addresses (for installing Scapy, use <code>pip3 install --pre scapy[basic]</code>)

## Reverse shell - reverse_shell
**reverse_shell.py**
- Reverse shell connecting to CNC server, receiving, and executing commands

**cnc_server.py**
- CNC server accepting client connections, sending commands, and displaying output

## Ransomware - ransomware
**ransomware.py**
- Demonstration of simple ransomware recursively iterating through a directory encrypting all files with a symmetric key, which is after encrypted with public key
- For generating RSA public key, use for example: <code>openssl genrsa -out rsa_pair.key 4096</code> and <code>openssl rsa -in rsa_pair.key -pubout -out rsa_public.key</code>
- Use at your own risk
