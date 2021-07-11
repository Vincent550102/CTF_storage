from Crypto.Util.number import *

n = 66473473500165594946611690873482355823120606837537154371392262259669981906291
e = 65537
p = 800644567978575682363895000391634967
q = 83024947846700869393771322159348359271173
phi = (p-1)*(q-1)

def decrypt(c, n, d):
    return pow(c,d,n)
if __name__ == '__main__':
    with open('flag.enc', 'rb', ) as fp:
        C = fp.read()
    print(C)
    c = bytes_to_long(C)
    print(c)
    d = inverse(e, phi)
    print(long_to_bytes(decrypt(c,n,d)))
