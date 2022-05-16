import myhash

game_str = "2,2"
hash = myhash.Hash()
h = hash.hexdigest(game_str.encode())
print(h)
