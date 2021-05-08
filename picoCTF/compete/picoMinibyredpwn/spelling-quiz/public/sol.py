import itertools

alphabet = list('abcdefghijklmnopqrstuvwxyz')

for p in list(itertools.permutations(alphabet)):
    print(p)
