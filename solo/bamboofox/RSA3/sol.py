p = 20931618958576754354721014153
q = 24201146151844603801115497273
n = p*q
phi = (p-1)*(q-1)
c = 288740973161309040787065319071174420184153482281597346181
from Crypto.Util.number import *
e = 65537
d = inverse(e,phi)
print(n)
print(long_to_bytes(pow(c,d,n)))