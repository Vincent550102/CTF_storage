cs= '''59 01 01 76 20 7C 01 74 3E 20 0B 01 07 20 05 01 7E 08 77 76 20 01 00 77 20 7F 01 04 77 20 75 7A 73 7E 7E 77 00 79 77 20 7B 00 20 0B 01 07 04 20 7C 01 07 04 00 77 0B 40 20 66 7A 7B 05 20 01 00 77 20 09 73 05 20 78 73 7B 04 7E 0B 20 77 73 05 0B 20 06 01 20 75 04 73 75 7D 40 20 69 73 05 00 39 06 20 7B 06 51 20 43 44 4A 20 7D 77 0B 05 20 7B 05 20 73 20 03 07 7B 06 77 20 05 7F 73 7E 7E 20 7D 77 0B 05 02 73 75 77 3E 20 05 01 20 7B 06 20 05 7A 01 07 7E 76 00 39 06 20 7A 73 08 77 20 06 73 7D 77 00 20 0B 01 07 20 06 01 01 20 7E 01 00 79 20 06 01 20 76 77 75 04 0B 02 06 20 06 7A 7B 05 20 7F 77 05 05 73 79 77 40 20 69 77 7E 7E 20 76 01 00 77 3E 20 0B 01 07 04 20 05 01 7E 07 06 7B 01 00 20 7B 05 20 01 7E 76 79 02 02 74 7E 73 75 79 75 40'''   
for bias in range(128):
    ans = ''
    for s in cs.split(' '):
        ans += chr((int(s,16)+bias)%128)     
    print()     
    print(ans)     