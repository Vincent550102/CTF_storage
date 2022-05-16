from pwn import *

r = process('TERM=xterm-256color ssh -p 5566 h173@quiz.ais3.org', shell=True, stdin=PTY)
r.interactive()
