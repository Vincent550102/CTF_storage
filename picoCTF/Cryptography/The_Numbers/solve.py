ll = [16,9,3,15,3,20,6,-1,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14,-1]
ans = ""
print("".join(chr(ord('A')+num-1) if num!=-1 else '{' for num in ll))
