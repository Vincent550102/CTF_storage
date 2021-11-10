from Crypto.Cipher import DES
import binascii
inputs = binascii.unhexlify('1234'.rstrip()).decode()
cipher = binascii.unhexlify('52241f58f8a213dd').rstrip()
enc_flag = binascii.unhexlify('af1e126eb6b7b77a34e45ab18525eec7149f1740e1119cbdad9f181caa4da5e904bf052c9df3bea9')

key_table = {}
def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        key1 = pad(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
                        ciph1 = DES.new(key1, DES.MODE_ECB)
                        enc_msg = ciph1.encrypt(pad(inputs))
                        key_table[enc_msg] = key1 
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        key2 = pad(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
                        ciph2 = DES.new(key2, DES.MODE_ECB)
                        if ciph2.decrypt(cipher) in key_table:
                            k1 = key_table[ciph2.decrypt(cipher)]
                            k2 = key2
                            c1 = DES.new(k2, DES.MODE_ECB)
                            eg = c1.decrypt(enc_flag)
                            c2 = DES.new(k1, DES.MODE_ECB)
                            print(c2.decrypt(eg))

