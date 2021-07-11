#!/usr/bin/env python3
import os
import random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode

with open("flag", 'rb') as data:
    flag = data.read().strip()

key = os.urandom(16)
def generate_counter():
    counter = random.randint(0,99)
    return counter.to_bytes(16, 'little')

def encrypt(message):
    aes = AES.new(key, AES.MODE_CTR, counter = generate_counter)
    return b64encode(aes.encrypt(message)).decode('ascii')

print("===== Welcome to nonsense machine =====")
print("Here is your flag : {}".format(encrypt(flag)))
print("Now I am going to talking nonsense")
print("You also need to tell me some nonsense")

while True:
    print(encrypt("nonsensenonsense"))
    input("your turn : ") # I don't care what you said XD
