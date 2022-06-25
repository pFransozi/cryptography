# Introduction

In cryptography, encryption is a cornerstone of data confidentiality and the effectiveness of cryptography is typically dependent on context. Cryptography is the primary tool for protecting information and it can be used to provide:

    1. confidentiality: only authorized parties can read the protected information. 
    2. authentication: you know that you are talking to the right entity/person and that they have not delegated their identity.
    3. integrity: a message hasn't been changed between the sender and receiver.

# Hashing

It involves the concept of an one-way f(x) or fingerprint, and only works well when:

    1. they produce repeadable, unique values for every input
    2. the output value provides no clues about the input that produced it.

When we talk about hashing in cryptography, we are talking about integrity. With a hashing process over a data we search for a way to guarantee the integrity of the data, which means if one bit chances the result hashing process will change as well. Take care, integrity is not confidentiality. When we talk about confidentiality, we are talking about that nobody but the authorized parties can read the message.

In hash vocabulary, digest is like a fingerprint: it is a small amount of data that stands in for the data's identity. Digests work the same way: given a document, it’s easy to calculate its digest; but given only a digest, it’s very hard to find out what document produced it. Very hard. The harder, the better, in fact.

Another point, hashing functions are lossy, which means information is lost from the source data to a digest or hash.

All hash functions have three characteristics, which are: consistency, compression, and lossiness. But a cryptographic hash function has more three: preimage resistance, second-preimage resistance, collision resistance.

## Preimage resistance

Preimage is the set of inputs for a hash function that produce a specific output. For instance, consider the even or odd function, all numbers that are even are preimage for the return 0 of the function, and all numbers that are odd, for the 1.

Preimage: A preimage for a hash function H and a hash value k is the set of values of
x for which H(x) = k. Considering that hash function receives a sequence of bits, so the preimage is the sequences of bits that digest the same result.

Preimage resistance is the difficult that a hash function gives to find a preimage correlated to a hash result.

The process of attempting to find an element in the preimage for a given output is called **inverting the hash**: trying to run it backward to get an input for a given output. Preimage resistance means that finding any inverse is hard.

Brute-force attack is an approach to try randomly sequences of bits as preimages to find the same hash function result.

## Second-preimage and collision resistance

So, as saw before: preimage resistance means it is really hard to find a data, sequence of bits, that produces a particular digest, unless you already know one.

Based on that, the second-preimage means that if you already have one data that produces a particular digest, it's still really hard to find a different data that produces the same digest. There is no exploitable pattern in the preimage.

Collision resistance means that it's hard to find any two inputs that produce the same output: not a specific output, just the same output. When a hash algorithm is resistant to collision, it is resistant to being able to purposefully create or pick any two inputs that produce the same digest, without deciding what that digest should be beforehand.

One property that helps with collision resistance is the fact that small changes in input can produce very large changes in output. For instance:

bob: 9f9d51bc70ef21ca5c14f307980a29d8
cob: 386685f06beecb9f35db2e22da429ec9

This is due to a property shared by many hashes and cryptographic ciphers called **the avalanche property**: a change to the input, no matter how small, creates a large and unpredictable change in the output. Ideally, 50% of the output bits should be altered for small input changes.

Remember that second-preimage resistance prevents you for finding a second member of the preimage for an output when you already have the first.

## Hash applicable

Do not use MD5. It has been deprecated for over 10 years, and some of its security flaws have been known for two decades.

Do not use SHA-1 because it is another algorithm that is relatively easy to create two inputs that hash to the same output.

A better option is SHA-256.

In Python is just a question of change the hasher:

import hashlib
hashlib.md5(b'alice').hexdigest()
'6384e2b2184bcbf58eccf10ca7a6563c'
hashlib.sha1(b'alice').hexdigest()
'522b276a356bdf39013dfabea2cd43e141ecc9e8'
hashlib.sha256(b'alice').hexdigest()
'2bd806c97f0e00af1a1fc3328fa763a9269723c8db8fac4f93af71db186d6e90'