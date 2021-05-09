from pwn import *

r = process("./pwntools")

r.recvuntil('er :)\n')

r.send(p32(0xdeadbeef))
r.recvline()

for _ in range(1000):
    q = r.recvuntil(' = ?').decode().replace(' = ?', '')
    ans = eval(q)
    print(ans)
    r.sendline(str(ans))
    print("ok")


r.interactive()
