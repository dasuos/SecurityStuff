## Ransomware - ransomware
**ransomware.py**
- **Use at your own risk.**
- Educational demo that recursively iterates through a directory, encrypting all files with a symmetric key, which is then encrypted with a public key
- For generating RSA private and public key, use for example: <code>openssl genrsa -out rsa_private.key 4096</code> and <code>openssl rsa -in rsa_pair.key -pubout -out rsa_public.key</code>

**decryption.py**
- The decryption of the symmetric key with the private key, which is used to decrypt all files in a directory recursively
