s = '21010011 32111 41021 5313 6220 7234 8163 953 a109 b47 c70 d3a e7b f49 g35 h5a i62 j2a k4f l4f m24 n48 o23 p3k q1n r47 s3b t3a u3k v1h w3p x1g y38 z3k'
li = s.split(" ")
print(li)
flag = ""
for c in li:
    con = c[1::]
    flag+=chr(int(con,int(c[0],36)))
    print(flag)
print(flag)