from base64 import *
from pwn import *
r = remote('140.110.112.215', 4119)
r.recvuntil(' : ')
flag_cipher = r.recvline().strip()

r.recvuntil('some nonsense\n')
print(flag_cipher)
r.recvline()
ans_list = []
for _ in range(300):
    r.recvuntil(' : ')
    r.sendline('')
    nonsense = b64decode(r.recvline().strip())
    k = xor('nonsensenonsense', nonsense)
    ans_list.append(xor(k,flag_cipher))
for i in ans_list:
    print(i)
    #MyFirstCTF{XNiDNI0UO2jcFxmKr7Ur}
