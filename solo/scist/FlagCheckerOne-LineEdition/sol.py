sss = [[9, 10, 23], [23, 22, 20], [14, 20, 4], [13, 12, 20], [8, 7, 20], [0, 3, 17], [9, 16, 24], [24, 8, 6], [18, 14, 11], [22, 15, 21], [2, 21, 0], [11, 9, 19], [5, 4, 3], [17, 11, 7], [19, 1, 21], [4, 11, 14], [12, 4, 20], [23, 21, 13], [3, 2, 15], [4, 12, 4]]
f =[251, 256, 300, 242, 263, 256, 328, 335, 269, 252, 263, 203, 291, 190, 220, 245, 277, 200, 214, 254]


flagstr = "SCIST{O4ObO4_7h3O_l4mbd4}"
flag = list()
for c in flagstr:
    flag.append(c)

for i in range(len(sss)):
    cnt = 0
    lost = 0
    sm = 0
    for ss in sss[i]:
        if(flag[ss]!='O'):
            cnt+=1
            sm+=ord(flag[ss])^7
        else:
            lost = ss
    if(cnt==2):
        guess = chr((f[i]-sm)^7)
        print(i,sm,f[i]-sm,guess,lost)
        flag[lost]=guess
print("".join(flag))
