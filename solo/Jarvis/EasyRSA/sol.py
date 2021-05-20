from Crypto.Util.number import *

c = 0xdc2eeeb2782c

N = 322831561921859 
p = 13574881 
q = 23781539
e = 23


phi = (p-1)*(q-1)
d = inverse(e,phi)

m = pow(c,d,N)
print(long_to_bytes(m))
