'''
An HMAC is a specific type of message authentication code (MAC) involving a cryptographic hash function and a secret cryptographic key. 
As with any MAC, it may be used to simultaneously verify both the data integrity and authenticity of a message. 
'''
import hmac

message = 'HMAC algorithm test with PYTHON'
key = 'PyTh0n'

hmac1 = hmac.new(key=key.encode(), msg=message.encode(), digestmod='sha1')
message_digest1 = hmac1.digest()
print("{} - Message Digest 1 : {}".format(hmac1.name, message_digest1))

hmac2 = hmac.new(key=key.encode(), digestmod='sha1')
hmac2.update(bytes(message, 'utf-8'))
message_digest2 = hmac1.digest()
print("{} - Message Digest 2 : {}".format(hmac1.name, message_digest1))

hmac3 = hmac.new(key=key.encode(), digestmod="sha1")
hmac3.update(bytes("Welcome to ", encoding="utf-8"))
hmac3.update(bytes("CoderzColumn.", encoding="utf-8"))
message_digest3 = hmac3.digest()

print("{} - Message Digest 3 : {}".format(hmac3.name, message_digest3))