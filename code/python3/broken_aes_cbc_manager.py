'''
This code has a problem that broke a principle of encryption.
EncryptionManager constructor method creates key and IV in each
class creation, and use those parameters every time until the class
is recreated.

IV is supposed to be different each time you encrypt, 
preventing the same data from being encrypted to the same ciphertext.

The issue is the same output for the same input. The best practice
is not reuse the same key.

'''

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class EncryptionManager:
    def __init__(self):
        self.key = os.urandom(32)
        self.iv = os.urandom(16)

    def encrypt_message(self, message):
        #this code is not secure!! It is just a theoretical exercise.

        encryptor = Cipher(
                        algorithms.AES(self.key),
                        modes.CBC(self.iv),
                        backend=default_backend()
        ).encryptor()
        padder = padding.PKCS7(128).padder()

        padded_message = padder.update(message)
        padded_message += padder.finalize()

        cipher_text = encryptor.update(padded_message)
        cipher_text = encryptor.finalize()

        return cipher_text

    def decrypt_message(self, ciphertext):
        # WARNING: This code is not secure!!
        decryptor = Cipher(
                algorithms.AES(self.key),
                modes.CBC(self.iv),
                backend=default_backend()
        ).decryptor()
        
        unpadder = padding.PKCS7(128).unpadder()
        padded_message = decryptor.update(ciphertext)
        padded_message += decryptor.finalize()
        message = unpadder.update(padded_message)
        message += unpadder.finalize()
        return message

manager = EncryptionManager()

plain_texts = [
            b'short',
            b'medium medium medium',
            b'long long long long long long'    
]

cipher_texts = []

for message in plain_texts:
    cipher_texts.append(manager.encrypt_message(message))

for cipher in cipher_texts:
    print('Recovered', manager.decrypt_message(cipher))