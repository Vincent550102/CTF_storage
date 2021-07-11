from Crypto.Util.number import getPrime

while True :
    inc = 15317023832913476369
    m = 14515602850859216993
    N = 16730460874151681213
    seed = 15017509946098832771
    if N > m and N > inc :
        break

def next_state(s0, m, inc, N):
    return (m*s0 + inc) % N

states = [seed]
for i in range(100) :
    seed = next_state(seed, m, inc, N)
    states.append(seed)

print(states[:20])
print(f"BreakAll{{{states[100]}}}")
