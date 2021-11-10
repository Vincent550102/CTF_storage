s = 'w1{1wq8/7376j.:'
flag = ''
for i in range(len(s)):
    if i%2:
        flag += chr(ord(s[i])+2)
    else:
        flag += chr(ord(s[i])-5)
print(flag)
