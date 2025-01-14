# ECRYP Project
## RC4 cipher
RC4 stands for Rivest Cipher 4 is a symmetric stream cipher developed by Ron Rivest from RSA
Security in 1987. This specific cipher is remarkable for its simplicity and speed in software
applications. However, toady this cipher is considered insecure due to many vulnerabilities
discovered years after its release.

RC4 cipher is based on Gilbert Vernams one-time pad cipher. So, as in Vernams cipher we are going
to XOR pseudorandom generated stream of numbers with original plaintext stream. Pseudorandom
generated stream in RC4 is obtained by use of secret internal state which consists of two parts. First,
a permutation of all 256 possible bytes, denoted by s and second, pair of 8bit index-pointers,
denoted by i and j. The permutation is initialized with a variable containing value of length of key,
using key-scheduling (KSA) algorithm. After that the stream of bits is generated using pseudo-random
generation algorithm (PRGA).

KSA algorithm is used to initialize the permutation in the array S. Key length is defined as the number
of bytes in the key and can be in the range 1 ≤ key length ≤ 256, typically between 5 and 16,
corresponding to a key length of 40-128 bits. First, the array S is initialized to the identity
permutation. S is then processed for 256 iterations in a similar way to the main PRGA, but also mixes
in bytes of the key at the same time.

In PRGA for as many iterations as needed it modifies the state and outputs a byte of the keystream.
In each iteration, the i is incremented, the values s[i] and s[j] are exchanged, then uses the sum
s[i]+s[j] (modulo 256) as an index to fetch a third element of s that is the keystream value of k below.
At the end of every iteration the bitwise exclusive XOR happens with the next byte of the message to
produce the next byte of either ciphertext or plaintext. So, every element of S is swapped with
another element of S at lest once in 256 iterations.
