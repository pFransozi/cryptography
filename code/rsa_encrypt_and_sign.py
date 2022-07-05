'''
It is important notice that a public key controls the encryption process, and the private key controls the correspondent decryption process. Ref. https://datatracker.ietf.org/doc/html/rfc3447#section-5.1
The private key must be used to control the process of signature, and the correspondent public key controlling the verification of that signature. Ref. https://datatracker.ietf.org/doc/html/rfc3447#section-5.2

The RSA.sign() uses the private key because the private key guarantee the authenticity.
The RSA.encrypt() uses the public key because the publick key guarantee the confidentiality.
'''
import base64
import rsa

def rsa_encryption():

    print()
    print()
    print()
    print('================================================================================')
    print('Encryption with RSA')
    print('================================================================================')

    public_key, private_key = rsa.newkeys(1024)

    message = 'Just a little test with encryption RSA.'
    encrypted_msg = rsa.encrypt(message.encode(), public_key)
    base64_msg = base64.b64encode(encrypted_msg).decode()

    print(f'Original message: {message}')
    print()
    print(f'Encrypted message: {encrypted_msg}')
    print()
    print(f'Encrypted message decoded: {base64_msg}')


    print('------------------------------------------------------------------------------')

    decrypted_msg = rsa.decrypt(encrypted_msg, private_key)

    print(f'Decrypted message with private key: {decrypted_msg.decode()}')


def rsa_signing():

    print()
    print()
    print()
    print("=======================================================================================")
    print("Signing with RSA")
    print("=======================================================================================")

    public_key, private_key = rsa.newkeys(1024)

    message = 'Just a little test with RSA signing'
    signature = rsa.sign(message.encode(), private_key, 'SHA-1')
    base64_signature = base64.b64encode(signature).decode()

    print(f'Original message: {message}')
    print()
    print(f'Signature: {signature}')
    print()
    print(f'Signature decoded: {base64_signature}')

    print("=======================================================================================")

    try:
        rsa.verify(message.encode(), signature, public_key)
    except  Exception as error:
        print(error)
    else:
        print('Signature verify.')
    


def main():
    rsa_encryption()
    rsa_signing()


if __name__ == '__main__':
    main()
