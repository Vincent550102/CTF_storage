import gmpy2
from Crypto.Util.number import *
E = 5502769663009776377079720669811
e = 65537
n = int(input("n: "))
X = 3

c2 = E*pow(X,e) % n
print("c2: {}".format(str(hex(c2))))
m2 = int(input("m2: "))
m = m2*inverse(X,n)
print("m: {}".format(str(m)))
