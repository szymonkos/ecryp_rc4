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

Schematic of the algorithm:
![schematic](https://upload.wikimedia.org/wikipedia/commons/e/e9/RC4.svg)

My implementation of RC4 in Python 3.8 requires additional library, NumPy. Thanks to that
operations on arrays are simpler and clearer.

Implementation:
```python
import numpy as np


def ksa(key):  # key-scheduling algorithm
    key_length = len(key)
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % key_length]) % 256
        s[i], s[j] = s[j], s[i]  # here we swap values of s[i] and s[j]
    return s


def gen(s, n):  # pseudo-random generation algorithm
    i = 0
    j = 0
    key = []
    while n > 0:
        n = n-1
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]  # here we swap values of s[i] and s[j]
        k = s[(s[i] + s[j]) % 256]
        key.append(k)
    return key


def create_key_array(s):
    return [ord(c) for c in s]


entered_key = input("Enter your key: ")
message = input("Enter your message: ")
entered_key = create_key_array(entered_key)
S = ksa(entered_key)
key_stream = np.array(gen(S, len(message)))
print("Key stream: ")
print(key_stream)  # here we print key_stream
print("Key stream in hexadecimal notation: ")
print(key_stream.astype(np.uint8).data.hex())  # here we print key stream in hexadecimal notation
message = np.array([ord(i) for i in message])
cipher = key_stream ^ message  # here we xor two arrays
print("Cipher in hexadecimal notation: ")
print(cipher.astype(np.uint8).data.hex())  # here we print cipher in hexadecimal notation
print("Cipher in unicode: ")
print([chr(c) for c in cipher])  # here we print cipher in unicode
```
Even though description and code of RC4 were leaked in 1994 and RC4 is no longer a trade secret,
still exact documentation of RC4 is restricted, so there are no officially available test vectors.
However, Wikipedia provides three test vectors, that are treated as perfect samples by community.

Table

Here are my results for keys and plaintexts given above:
```
Enter your key: Key
Enter your message: Plaintext
Key stream:
[235 159 119 129 183  52 202 114 167]
Key stream in hexadecimal notation:
eb9f7781b734ca72a7
Cipher in hexadecimal notation:
bbf316e8d940af0ad3
Cipher in unicode:
['>>', 'ó', '\x16', 'ę', 'U', '@', '_', '\n', 'Ó']

Process finished with exit code 0
```

```
Enter your key: Wiki
Enter your message: pedia
Key stream:
[ 96  68 219 109  65]
Key stream in hexadecimal notation:
6044db6d41
Cipher in hexadecimal notation:
1021bf0420
Cipher in unicode:
['\x10', '!', '?', '\x04', ' ']

Process finished with exit code 0
```

```
Enter your key: Secret
Enter your message: Attack at dawn
Key stream:
[  4 212 107   5  60 168 123  89  65 114  48  42 236 155]
Key stream in hexadecimal notation:
04d46b053ca87b594172302aec9b
Cipher in hexadecimal notation:
45a01f645fc35b383552544b9bf5
Cipher in unicode:
['E', '\xa0', '\x1f', 'd', '_', 'Ą', '[', '8', '5', 'R', 'T', 'K', '\x9b', 'ó']

Process finished with exit code 0
```
