table = dict()
for i in range(26):
    table[chr(ord('A')+i)] = dict()
    for j in range(26):
        table[chr(ord('A')+i)][chr(ord('A')+j)] = chr((i+j)%26+ord('A'))
#print([i for i in table])
#print(table['T']['U'])

key = "SOLVECRYPTO"
flg = "UFJKXQZQUNBi"
ans = ""
for idx,k in enumerate(key):
    for nk in table[k]:
        if table[k][nk]==flg[idx]:
            ans+=nk
print(ans)
