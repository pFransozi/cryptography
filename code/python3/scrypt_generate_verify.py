'''
This is an example how to use the scrypt algorithm. It is a highly recommended algorithms for password storage describe in RFC 7914.
'''
import os
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.hazmat.backends import default_backend

salt = os.urandom(16)

kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
key = kdf.derive(b'MyGr34tP@ssword')

kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1, backend=default_backend())
kdf.verify(b'MyGr34tP@ssword', key)

print("Success! (Exception if mismatch)")
