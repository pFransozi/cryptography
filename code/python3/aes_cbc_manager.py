'''
Cryptography module use the update/finalize pattern because 
quite often data needs to be processed in chunks in many practical
cryptographic operations such as network transmitting or
encrypting a local file on the hard drive.

'''

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class EncryptionManager:
    def __init__(self):
        key = os.urandom(32)
        iv = os.urandom(16)
        aesContext = Cipher(
            algorithms.AES(key),
            modes.CBC(iv),
            backend=default_backend()
        )

        self.encryptor = aesContext.encryptor()
        self.decryptor = aesContext.decryptor()
        self.padder = padding.PKCS7(128).padder()
        self.unpadder = padding.PKCS7(128).unpadder()

    def update_encryptor(self, plain_text):
        return self.encryptor.update(self.padder.update(plain_text))

    def finalize_encryptor(self):
        return self.encryptor.update(self.padder.finalize()) + \
        self.encryptor.finalize()

    def update_decryptor(self, ciphertext):
        return self.unpadder.update(self.decryptor.update(ciphertext))

    def finalize_decryptor(self):
        return self.unpadder.update(self.decryptor.finalize()) + \
            self.unpadder.finalize()

manager = EncryptionManager()

plain_texts = [
    b'short',
    b'medium medium medium',
    b'long long long long long long'
]

cipher_texts = []

for message in plain_texts:
    cipher_texts.append(manager.update_encryptor(message))
cipher_texts.append(manager.finalize_encryptor())

for cipher in cipher_texts:
    print('Recovered', manager.update_decryptor(cipher))
print('Recovered', manager.finalize_decryptor())