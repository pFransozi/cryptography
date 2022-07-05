# Symmetric Encryption

Symmetric encryption is at the foundation of all modern secure communications based on the same key used to encrypt is used to decrypt.

Encryption, related to a symmetric process, is all about confidentiality, which means that only folks with the right key are able to read the data. Then, the message is protected from the outsiders.

The fact that the message is protected from outsiders does not guarantee that que encrypted message be altered, which means, violation of the integrity.

### aes, symmetric block cipher

The idea behind symmetric encryption is that the same key is used for both encryption and decryption. Symmetric key encryption algorithms are often divided into two subtypes: **block ciphers and stream ciphers**. A block cipher gets its name from the fact that it works on blocks of data: you have to give it a certain amount of data before it can do anything, and larger data must be broken down into block-sized chunks (also, every block must be full). Stream ciphers, on the other hand, can encrypt data one byte at a time. **AES is fundamentally a symmetric key, block cipher algorithm**.

It is used in many common Internet protocols and operating system services, including **TLS (used by HTTPS)**, **IPSec**, and **file-level** or **full-disk encryption**. Given its ubiquity, it is arguably the most important cipher to know how to use properly. More importantly, the principles of correct use of AES transfer easily to correct use of other ciphers.

AES has several modes of operation, such as:

1. electronic code book (ECB), obsolete
2. Cipher block chaining (CBC)
3. counter mode (CTR)
4. GCM, recommended instead of the above

### EBC

It is not recommended, but can be used in a didatic way to understanding the background of AES. EBC is a raw AES that **treats every 16-byte block (128-bits block) of data independently, encrypting each one in exactly the same way using provided key**. **The weakness of EBC is in independence property**.

AES in its raw mode is like a code book. For every input and key, **there is exactly one output**, **independent of any other inputs**. Based on that independent principle, an attacker can break the code comparing, for instance, discarted encrypted message looking for patterns.

A common error made by those trying to protect information **is to assume that the enemy cannot know some detail about how the system works**. Always live by Kerckhoff’s principle: a cryptographic system must be secure even if everything is known about it, except the key.

**Based on EBC weakness, it can be deduces**:

1. encrypt the same emssage differently each time
2. eliminate predictable patterns between blocks

To solve the first issue, it is used a technique called **initialization vector or IV**. An IV is typically **a random string that is used as a third input—in addition to the key and plaintext—into the encryption algorithm**. Exactly how it is used depends on the mode, but the idea is to prevent a given plaintext from encrypting to a repeatable ciphertext. Unlike the key, the IV is public. That is, one assumes that an attacker knows, or can obtain, the value of the IV. The presence of an IV doesn’t help to keep things secret so much as it helps to keep them from being repeated, avoiding exposure of common patterns.

As for the second problem, that of being able to eliminate patterns between blocks, we will solve it by introducing new ways to encrypt the message as a whole, rather than treating each block as an individual, independent mini-message like ECB mode does.

To improve ECB, the method should have the avalanche property, similar to hash method property, which means when a bit from the origin data, more than half in the result data must change. AES does it, but ECB mode no.

**Cipher block chaining (CBC) mode** is a method that ciphertext of one block affect all subsequent blocks. When encrypting, one can XOR the encrypted output of a block with the unencrypted input of the next block.

XOR, just to remember, has the folowing true table:

0 xor 0 = 0
0 xor 1 = 1
1 xor 0 = 1
1 xor 1 = 0

Then, CBC xor the output of one block of ciphertext with the next plaintext block. Therefore, changes to any input block affect the output block for all subsequent blocks.

