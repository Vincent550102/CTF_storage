from pwn import *

r = remote('103.147.23.70', 65431)

r.recvline()
r.recvline()
for i in range(40):
    eq = r.recvline().strip().split('=')[0]
    ans = eval(eq)
    print(ans)
r.interactive()
