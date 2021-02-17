message = "gvswwmrkxlivyfmgsrhnrisegl"
for bias in range(27):
    print("".join(chr((ord(_)+bias-ord('a'))%26+ord('a')) for _ in message))

