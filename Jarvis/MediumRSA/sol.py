#coding:utf-8
from Crypto.Util.number import *
import binascii

n = 87924348264132406875276140514499937145050893665602592992418171647042491658461

p = 275127860351348928173285174381581152299

q = 319576316814478949870590164193048041239

phi = (p-1)*(q-1)

e = 65537

d = inverse(e,phi)

with open('./flag.enc','rb') as f:
    c = binascii.hexlify(f.read())
    c = int(c.decode(),16)

m = pow(c,d,n)

print(long_to_bytes(m))
