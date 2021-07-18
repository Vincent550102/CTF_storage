from pwn import *
r = remote('konkonkon.misc.quals.r2s.tw',3333)
r.recvline()
r.recvline()
r.sendline('Kon?!OuO')
r.sendline('read_flag')

r.recvline()
r.recvline()
r.recvline()

mat = eval(r.recvline().replace(' = ?',''))
print(mat)
r.interactive()
r.sendline(str(mat))
r.interactive()
