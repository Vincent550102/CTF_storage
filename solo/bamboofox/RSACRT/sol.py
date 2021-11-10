from Crypto.Util.number import *
from functools import reduce
import operator
e = 3
n1 = 101290671645891113443178779921367512224722901166866303284054622650913882237943
c1 = 17573203065232275223032959594073714865227647588040103112741970978754528744412

n2 = 62253885479193154605424195014579318487651384340805144136474228530384884231371
c2 = 41673368189713324195727344706907979718347285911470053778688935001264046241730

n3 = 67229667686832315756851959770256442621746487728232323452108661943500004703577
c3 = 22517810114157946845060101815805705621035921616256336505911033087991816584002
def crt(remainders, modules):
    """
    Solving Chinese Remainder Theorem
    @modules and @remainders are lists.
    """
    x = 0
    N = reduce(operator.mul, modules)
    for i, module in enumerate(modules):
        if module == 1:
            continue
        Ni = N // module
        b = inverse(Ni, module)
        x += remainders[i] * Ni * b
    return x % N


m = crt([c1,c2,c3], [n1,n2,n3])

from gmpy2 import iroot

print(long_to_bytes(iroot(m,3)[0]))
