from pwn import *
from time import sleep
r = remote('quiz.ais3.org', 2222)

DATA = "502848906b66f5e994a1a62dbaee21012575ddf72c2fa9c83d46206b9252252b00ffb5981de06e4f616acf1d78beba67efeea88773d28086d0199c4011991ac42fdb525deefb2cd806f8b0d8790ca679dd09ce0a3276c3175b2f66ac4c1c39b2226e8808501a2190dd776953df43f203"
r.send("asd\n")
cnt = 0
while True:
    cnt+=1
    r.sendline('L')
    r.sendline(DATA)
    r.sendline()
    r.sendline('B')
    r.recvuntil('[Shop]')
    r.sendline('B')
    r.recvuntil('(H)')
    context = r.recvuntil('(H)')
    if "-2147483647" not in context:
        break
    r.sendline('Q')
    log.info(str(cnt))
r.interactive()

#5103e36ee154d485f2b20e47997b689c2575ddf72c2fa9c83d46206b9252252b00ffb5981de06e4f616acf1d78beba67efeea88773d28086d0199c4011991ac42fdb525deefb2cd806f8b0d8790ca679dd09ce0a3276c3175b2f66ac4c1c39b2765af9692b2cabc23cd9684f34a0579a
