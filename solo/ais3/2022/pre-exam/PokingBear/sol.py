import requests
url = 'http://chals1.ais3.org:8987/bear/{}'

for i in range(350,777):
    r = requests.get(url.format(str(i)))
    if "This is not even a bear." not in r.text:
        print(str(i))
