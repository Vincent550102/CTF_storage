e = 3
n = 1167197297168197224115084199925099795845243071360935570640315801827789019983670634989467231207397
c = 145466097414922906240056239374070683001644863307103240158288639101506732073374851114168168037

from gmpy2 import iroot
from Crypto.Util.number import *

for k in range(100000000):
    tmp = c+k*n
    m, ok = iroot(tmp, e)
    if ok:
        print(long_to_bytes(m))
        print(m)