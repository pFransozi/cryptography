# Hashing

It involves the concept of an one-way f(x) or fingerprint, and only works well when:

    1. they produce repeadable, unique values for every input
    2. the output value provides no clues about the input that produced it.

When we talk about hashing in cryptography, we are talking about integrity. With a hashing process over a data we search for a way to guarantee the integrity of the data, which means if one bit changes the result hashing process will change as well. **Take care, integrity is not confidentiality**. When we talk about confidentiality, we are talking about that nobody but the authorized parties can read the message.

In hash vocabulary, digest is like a fingerprint: **it is a small amount of data that stands in for the data's identity**. Digests work the same way: given a document, it’s easy to calculate its digest; but given only a digest, it’s very hard to find out what document produced it.

Another point, hashing functions are lossy, which means information is lost from the source data to a digest.

All hash functions have three characteristics, which are: consistency, compression, and lossiness. But a cryptographic hash function has more three: preimage resistance, second-preimage resistance, collision resistance.

## Preimage, second-preimage and collision resistance

**Preimage resistance** 
It is the set of inputs for a hash function that produce a specific output. For instance, consider the even or odd function, all numbers that are even are preimage for the return 0 of the function, and all numbers that are odd, for the 1. **A preimage** for a hash function H and a hash value k is the set of values of x for which H(x) = k. Considering that hash function receives a sequence of bits, so the preimage is the sequences of bits that digest the same result. **Preimage resistance is the difficult that a hash function gives to find a preimage correlated to a hash result**. The process of attempting to find an element in the preimage for a given output is called **inverting the hash**: trying to run it backward to get an input for a given output. **Preimage resistance means that finding any inverse is hard**. Brute-force attack is an approach to try randomly sequences of bits as preimages to find the same hash function result.

**Second-preimage and collision resistance**
So, as saw before, preimage resistance means **it is really hard to find a data, sequence of bits, that produces a particular digest**, unless you already know one. Based on that, the second-preimage means that if you already have one data that produces a particular digest, **it's still really hard to find a different data that produces the same digest**. There is no exploitable pattern in the preimage.

**Collision resistance means that it's hard to find any two inputs that produce the same output**: not a specific output, just the same output. When a hash algorithm is resistant to collision, **it is resistant to being able to purposefully create or pick any two inputs that produce the same digest**, without deciding what that digest should be beforehand. One property that helps with collision resistance is the fact that small changes in input can produce very large changes in output. For instance:

bob: 9f9d51bc70ef21ca5c14f307980a29d8
cob: 386685f06beecb9f35db2e22da429ec9

This is due to a property shared by many hashes and cryptographic ciphers called **the avalanche property**: a change to the input, no matter how small, creates a large and unpredictable change in the output. Ideally, 50% of the output bits should be altered for small input changes. Remember that second-preimage resistance prevents you for finding a second member of the preimage for an output when you already have the first.

## Hash applicable

**Do not use MD5**. It has been deprecated for over 10 years, and some of its security flaws have been known for two decades. **Do not use SHA-1** because it is another algorithm that is relatively easy to create two inputs that hash to the same output. A better option is SHA-256.

In Python is just a question of change the hasher:

import hashlib
hashlib.md5(b'alice').hexdigest()
'6384e2b2184bcbf58eccf10ca7a6563c'
hashlib.sha1(b'alice').hexdigest()
'522b276a356bdf39013dfabea2cd43e141ecc9e8'
hashlib.sha256(b'alice').hexdigest()
'2bd806c97f0e00af1a1fc3328fa763a9269723c8db8fac4f93af71db186d6e90'

## Hash passwords

Using hash for passwords is a good idea, but take care about **the deterministic factor**, which means, even though the hash used is without known vulnerabilities, an attacker can determine the value because **a hash function generates the same output from the same input**. If the attacker has a rainbow table with the most common password in SHA-256, **it is possible for him determines a reverse engineering**. For instance:

data stolen: 5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8
rainbow table: sha256('password') == '5E884898DA28047151D0E56F8DC6292773603D0D6AABBDD62A11EF721D1542D8'

**That is where the salt comes into play**. A salt is a publicly known value that is mixed in with the user’s password before hashing. By mixing in a salt value, the user’s password will not be immediately discernible. **This salt has to be chosen correctly**. It needs to be **unique**, and it needs to be **sufficiently long**. One way of doing this is to use os.urandom and base64.b64encode. **Once you have the salt, you store it, then mix the password and the salt with concatenation**.

**It should be easy to see that the same salt has to be used every time for checking a user’s password**. **But should the same salt be used for multiple users?** **Could you generate the salt once for an entire web site and just reuse it?** The answer is a very strong “No!” Can you think of why? What will be the impact if two users are using the same salt? At the very least, it means that it is instantly easy to recognize if two users are sharing the same password. 

Additionally, best practice is to store the user name and salt along with the password hash: smithj,cei6LtJVQYSM+n6Cty0O2w==, bd51dac1e2fca8456069f38fcce933f1ff30a656320877b596a14a0e05db9567

There are three highly recommended algorithms for password storage:

1. scrypt, more in RFC 7914
2. bcrypt, more in https://pypi.org/project/bcrypt/
3. argon2, more in https://pypi.org/project/argon2/

Example how to use scrypt, [scrypt python code](scrypt_generate_verify.py).

## Proof of Work

Another area where hashing is used extensively is so-called “proof-of-work” **schemes in blockchain technologies**. The basic idea of a blockchain is a “distributed ledger.” The system is a ledger because
it records information related to transactions between participants. It can also store additional information, but the primary operations are transactions. It is a distributed ledger because its contents are stored across the set of participants and not in any central location. **Every transaction must be stored in a block, which is just a collection of data**. Each transaction within the block must be digitally signed by the transactor, **with his private key**, **and the overall block structure is protected by a hash**.

The designer of Bitcoin wanted to control **how quickly new blocks could be created and also wanted the system to incentivize participation**. The solution was to award bitcoins to the “miner” that produced a new block while making the production of the new block very difficult. **Basically, at any given time, various parties known as miners are searching for the next block in the blockchain**. Any user of blockchain can request a transaction. They broadcast their desired transaction throughout the blockchain network and miners will pick them up. The miners take some set of requested transactions (there is a limited number per block) and create a candidate block. This candidate block has all the right pieces of information. It has the transactions, the metadata, and so forth. **But it isn’t the next block in the blockchain until the miner can solve a cryptographic puzzle**. 

**That puzzle is to find a special kind of SHA-256 hash value, specifically a value smaller than a certain threshold**. Finding an input that produces one particular output would take a really, really long time, **but finding any output less than a certain value takes a lot less time**. Making that threshold smaller reduces the number of valid hashes, requiring more work to find a suitable value, and that’s how Bitcoin adjusts the difficulty to account for faster hardware or larger computational pools as time goes on. Ultimately, it takes about 10 minutes for the entire Bitcoin network to find a suitable hash. If it takes less than that on average over a period of weeks, the maximum allowed hash value is decreased.
