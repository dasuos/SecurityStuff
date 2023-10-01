## Ransomware - ransomware
**ransomware.py**
- Ransomware recursively iterating through a directory encrypting all files with a symmetric key, which is after encrypted with a public key
- For generating RSA private and public key, use for example: <code>openssl genrsa -out rsa_private.key 4096</code> and <code>openssl rsa -in rsa_pair.key -pubout -out rsa_public.key</code>
- Use at your own risk

**decryption.py**
- The decryption of symmetric key with private key, which is after that used to recursively decrypt all files in a directory
