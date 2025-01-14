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
