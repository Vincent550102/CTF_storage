f= [166, 32, 178, 20, 188, 74, 42, 238, 34, 200, 162, 100, 12, 98, 4, 186, 210, 14, 198, 120, 24, 156, 16, 186, 208, 86, 62, 80, 54, 204]
flag = ""
for i in range(0,len(f)):
    if not i: 
        continue
    flag+=chr((f[i-1]//2)^f[i]//2)
print(flag)

