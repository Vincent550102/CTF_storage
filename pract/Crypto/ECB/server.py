#!/usr/bin/env python3
import os
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from flag import flag

key = os.urandom(16)

aes = AES.new(key, AES.MODE_ECB)

def pad(data):
    k = -len(data) % 16
    if k == 0: k = 16
    return data + bytes([k] * k)

def unpad(data):
    return data[:-data[-1]]

def encrypt(data):
    return aes.encrypt(pad(data))

def decrypt(data):
    return unpad(aes.decrypt(data))

def register():
    username = input('username: ').strip()
    if 'admin' in username:
        exit()
    password = input('password: ').strip()
    token = encrypt(f'username:{username};password:{password}'.encode())
    print(b64encode(token).decode())

def login():
    token = decrypt(b64decode(input('token: ')))
    username, password = token.split(b';')
    if username.split(b':')[1] == b'admin':
        print(flag)

def menu():
    print('''1) register
2) login''')

def main():
    while True:
        menu()
        option = input('> ').strip()
        if option == '1':
            register()
        elif option == '2':
            login()
        else:
            exit()

main()
