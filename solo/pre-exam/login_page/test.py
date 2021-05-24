import json

a = input()
b = input()

data = '{"showflag": false, "username": "%s", "password": "%s"}' % (a,b )

user = json.loads(data)
print(user)
