from Crypto.Util.number import *

p = 3487583947589437589237958723892346254777 
q = 8767867843568934765983476584376578389
e = 65537

phi = (p-1)*(q-1)

#d*e%phi=1

d = inverse(e,phi)
print(d)
