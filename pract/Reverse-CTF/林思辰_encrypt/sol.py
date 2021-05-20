s = 'zGs7@ABp"sIp/3bn@-:A-G]CllNNK'
'''
for bia in range(0,129):
    ans = ''
    for c in s:
        ans+= chr((ord(c)+bia)%128 )
    print(bia, ans)
'''

ans = ''
for i in range(len(s)):
    if i in [0,2,7,9,14,16,21,23,28,30]:
        ans+=chr((ord(s[i])+83)%128)
        print((ord(s[i])+51)%128)
    else:
        ans+=chr((ord(s[i])+50)%128)
        print((ord(s[i])+50)%128)
print(ans)
