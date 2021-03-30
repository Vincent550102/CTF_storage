flaged = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸強㕤㐸㤸扽'
#print(''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)]))
flag = ''
for f in flaged:
    flag+=chr(ord(f)//256)
    flag+=chr(ord(f)%256)
print(flag)
