import random

def modpow(b, e, m):
    result = 1
    e = int(e)
    while e != 0:
        if e % 2 != 0:
            e -= 1
            result = (result * b) % m
            continue
        e >>= 1
        b = (b * b) % m
    return result

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def ext_gcd(a,b): 
    if(b==0): 
        return 1, 0
    else: 
        x, y = ext_gcd(b, a%b)
        x, y = y, (x-(a//b)*y)
        return x, y
if __name__ == "__main__":
    p = 170141183460469231731687303715884105727
    q = 17 
    N=p*q
    phi = (p-1)*(q-1)
    e=0


    while(True):
        e = random.randint(2, phi)
        if gcd(e, phi)==1:
            break
    # public (e, N)
    # privial (d, N)

    d = ext_gcd(e,phi)[0]

    plaintext = input()

    encrytext = modpow(plaintext, e, N)

    print("phi {}".format(phi))
    print("plaintext {}".format(plaintext))
    print("e {}".format(e))
    print("encrytext {}".format(encrytext))
    print("d {}".format(d))

    plaintext = modpow(encrytext, d, N)

    print("plaintext {}".format(plaintext))


