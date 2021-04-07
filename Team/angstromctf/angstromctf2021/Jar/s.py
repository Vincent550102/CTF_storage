import socket

bind_ip = "127.0.0.1"
bind_port = 8080

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

server.listen(5)

print "[*] Listening on %s:%d " % (bind_ip,bind_port)

while True:
    client,addr = server.accept()
    print 'Connected by ', addr

    while True:
        data = client.recv(1024)
        print "Client recv data : %s " % (data)

        client.send("ACK!")
