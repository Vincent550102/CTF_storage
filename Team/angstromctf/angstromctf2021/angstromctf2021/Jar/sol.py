

import pickle
import base64
flag = "flag{}"
items = []
byte = pickle.loads(base64.b64decode('YwAAAAAAAAAAAQAAAEMAAABzDQAAAHQAAGcBAGEBAGQAAFMoAQAAAE4oAgAAAHQEAAAAZmxhZ3QFAAAAaXRlbXMoAAAAACgAAAAAKAAAAABzBgAAAHNvbC5weXQEAAAAc2NyaQ8AAABzAgAAAAAC'))
#print(byte)

print(items)

'''
import marshal
import base64
def scri():
    global items
    items = [flag]
print(base64.b64encode(marshal.dumps(scri.func_code)))
'''
