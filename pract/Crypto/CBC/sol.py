from base64 import b64encode, b64decode
from pwn import *

r = remote('140.110.112.215', 4120)

en = b64decode(r.recvline().strip())
print(en)
iv, b1, b2, pad = (en[:16], en[16:32], en[32:48], en[48:64])

zero = xor(b1, 'A'*16)
payload = xor(zero, 'CTFGOGOGO\x00\x00\x00\x00\x00\x00\x00')

res = b64encode(iv + payload + b2 + pad)

r.sendline(res)


r.interactive()
