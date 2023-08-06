from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.fernet import Fernet
from pathlib import Path
import sys

private_key_path = sys.argv[1]
encrypted_symmetric_key_path = sys.argv[2]
directory_path = sys.argv[3]

# load private key for decryption of symmetric key
with open(private_key_path, 'rb') as file:
    private_key = serialization.load_pem_private_key(
        file.read(),
        password=None,
        backend=default_backend()
    )

with open(encrypted_symmetric_key_path, 'rb') as encrypted_symmetric_key_file:
    # decrypt encrypted symmetric key
    symmetric_key = private_key.decrypt(
        encrypted_symmetric_key_file.read(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # recursively decrypt all encrypted files in a directory
    fernet = Fernet(symmetric_key)
    for item in Path(directory_path).rglob('*'):
        if item.is_file():
            with open(item, 'rb') as file:
                plaintext = fernet.decrypt(
                    file.read()
                )
            with open(item, 'wb') as file:
                file.write(plaintext)
