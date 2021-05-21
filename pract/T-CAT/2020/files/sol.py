from Crypto.Util.number import *
e = 252323
N = 13886599
c = 7217220

p=3259
q=4261
phi=(p-1)*(q-1)
d = inverse(e,phi)

print(long_to_bytes(pow(c,d,N)))

