import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
en = 'ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih'

def b16_decode(plain):
    ans = ''
    for i in range(0,len(en),2):
        n_word=int()
