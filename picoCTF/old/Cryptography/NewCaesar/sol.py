import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
en = 'ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih'

def b16_decode(plain):
    ans = ''
    #print(plain)
    for i in range(0,len(plain),2):
        assert(i<len(plain))
        t1 = ord(plain[i]) - LOWERCASE_OFFSET
        t2 = ord(plain[i+1]) - LOWERCASE_OFFSET
        #print(origin_word)
        ans+=chr(t2+t1*16)
        #ans += chr(int(origin_word,2))
    return ans

def b16_encode(plain):
	enc = ""
	for c in plain:
                binary = "{0:08b}".format(ord(c))
                #print(binary)
                enc += ALPHABET[int(binary[:4], 2)]
                enc += ALPHABET[int(binary[4:], 2)]
                #print(enc)
	return enc

def unshift(c,k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = k
    return ALPHABET[(t1-t2+16)%16]

'''
test = b16_encode('hello')
print(test)
print(b16_decode(test))
'''

for k in range(16):
    shifted = "".join(unshift(c,k) for c in en) 
    print(k, b16_decode(shifted))
