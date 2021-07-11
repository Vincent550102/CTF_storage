#!/usr/bin/env python3
import os
from base64 import b64encode, b64decode
from Crypto.Cipher import AES

flag = open('flag', 'r').read()
key = os.urandom(16)

def pad(data):
    k = -len(data) % 16
    if k == 0: k = 16
    return data + bytes([k] * k)

def unpad(data):
    return data[:-data[-1]]

def encrypt(data):
    iv = os.urandom(16)
    aes = AES.new(key, AES.MODE_CBC, iv = iv)
    return iv + aes.encrypt(pad(data))

def decrypt(data):
    iv, data = data[:16], data[16:]
    aes = AES.new(key, AES.MODE_CBC, iv = iv)
    return unpad(aes.decrypt(data))

print(b64encode(encrypt(b'A' * 32)).decode())

cipher = b64decode(input().strip())
if b'CTFGOGOGO' in decrypt(cipher):
    print(flag)
