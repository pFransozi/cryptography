from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

key = os.urandom(32)
iv = os.urandom(16)

aesCipher = Cipher(algorithms.AES(key),
                    modes.CBC(iv),
                    backend=default_backend())

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

plain_texts = [
            b'short', 
            b'medium medium medium',
            b'long long long long long long'
        ]

cipher_texts = []

'''
Update() does not send to encryption the input data in each time
it is called, but a concatenation of every input data for some
number of update() calls. And finalize() call at the end.

That is similar with padder.update(), each it is called a string
is concatenated. PKCS7 padding does not add any padding until the finalize
operation
'''

for message in plain_texts:
    padded_message = padder.update(message)
    cipher_texts.append(aesEncryptor.update(padded_message))

cipher_texts.append(aesEncryptor.update(padder.finalize()))

for cipher in cipher_texts:
    padded_message = aesDecryptor.update(cipher)
    print('recovered', unpadder.update(padded_message))

print('recovered', unpadder.finalize())