import requests
URL = 'http://www.wechall.net/challenge/training/programming1/index.php?action=request' 
U = 'http://www.wechall.net/challenge/training/programming1/index.php?answer='
c = {"WC":"13241299-58491-gSFaKs9WzaJTANqz"}
ans = requests.get(URL, cookies=c).text
requests.get(U+ans,cookies=c)
