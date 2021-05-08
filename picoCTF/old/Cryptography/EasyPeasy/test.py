from pwn import *
en_flag='0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d'
rul =   '0351533d190256152d3d195059113d1959523d1904513d19515311253d195803'
ui = 'a'*32
rul_parse = [rul[i]+rul[i+1] for i in range(0,len(rul),2)]
flag_parse = [en_flag[i]+en_flag[i+1] for i in range(0,len(en_flag),2)]

print(len(rul_parse))

key = list(map(lambda p, k: int(p,16)^ord(k), rul_parse, ui))
print(key)
ans = ("".join(list(map(lambda p, k: chr(int(p,16)^k) , flag_parse, key))))
print(ans)
for a in ans:
    print(ord(a),a)
result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ans, key))
print("".join(result))
#_=\x0eB,d\A$eY\x1c<\x0cxb[0-\x00}e\x0f]"Y%
