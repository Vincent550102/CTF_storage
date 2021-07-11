from secret import FLAG
from Crypto.Util.number import bytes_to_long
from Crypto.Util.number import getStrongPrime, isPrime, inverse

m = bytes_to_long(FLAG)
q = p = getStrongPrime(1024)

while True :
    q += 1
    if isPrime(q) : 
        break

n = p*q
e = 65537

c = pow(m,e,n)
phi = (p-1) * (q-1)
d = inverse(e, phi)
assert pow(c,d,n) == m

print(f"n = {n}")
print(f"e = {e}")
print(f"c = {c}")