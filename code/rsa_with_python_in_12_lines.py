'''
Ref: Buchanan, William J (2022). RSA in 12 lines of Python. Asecuritysite.com. https://asecuritysite.com/rsa/rsa12

https://www.comparitech.com/blog/information-security/rsa-encryption/ 

'''
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes 
import Crypto
import libnum

bits=2048
msg="goodbye"

p = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)
q = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)

# operation over the prime numbers
n = p*q
PHI=(p-1)*(q-1)

e=65537
d=libnum.invmod(e,PHI)

m=  bytes_to_long(msg.encode('utf-8'))

c=pow(m,e, n)
res=pow(c,d ,n)

print ("Message=%s\np=%s\nq=%s\n\nd=%d\ne=%d\nN=%s\n\nPrivate key (d,n)\nPublic key (e,n)\n\ncipher=%s\ndecipher=%s" \
             % (msg,p,q,d,e,n,c,(long_to_bytes(res))))