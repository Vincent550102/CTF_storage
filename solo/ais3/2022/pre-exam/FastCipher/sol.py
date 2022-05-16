import binascii
ct = []
for a in binascii.unhexlify("6c0ec840f88d4cd7fcc6d5c6d1dafcc1cad7d0fcc2d1c6fcd6d0c6c7fccfcccfde"):
    ct.append(a)
M = 2**1024

def f(x):
    return (
        4 * x**4 + 8 * x**8 + 7 * x**7 + 6 * x**6 + 3 * x**3 + 0x48763
    ) % M

num = ct[1]
key = 45
flag = ""
for c in ct:
    flag+=chr(c ^ (key&0xFF))
    key = f(key)

print(flag)
