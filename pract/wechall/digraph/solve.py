/bin/bash: :q：命令找不到
        }
for part in s.split(' '):
    ans = ''
    for c in range(0,len(part),2):
        now = part[c]+part[c+1]
        if now in dic:
            ans+=dic[now]
        else:
            ans+='?'
        print("{} ".format(now))
    print('')
    print(ans)
    print('')
