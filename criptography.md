
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