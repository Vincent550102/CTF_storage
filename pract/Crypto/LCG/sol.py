from functools import reduce
from math import gcd
from Crypto.Util.number import inverse
def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * inverse(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(gcd, zeroes))
    return crack_unknown_multiplier(states, modulus)

stat = [
15017509946098832771,
15124579160039492440,
15472925640891320616,
38114629134274242,
2948866201570354398,
3753737287032175650,
15046504952114087560,
194647690542408530,
1225780854132722636,
4013014980629339934,
13449159198226705850,
14220130235020001721,
13183859804543703356,
11850731162465520686,
8189996643791134442,
11962273554780984216,
11975201758538349117,
1433420360059014742,
16167029535121166235,
4937294321112803794
]

print(crack_unknown_modulus(stat))

