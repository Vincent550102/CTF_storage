import wave
import numpy as np
def byte_xor(ba1, ba2):
    return bytes([abs(_b - _a) for _a, _b in zip(ba1, ba2)])

r1 = wave.open('./o1.wav', mode='rb')
r2 = wave.open('./o2.wav', mode='rb')

frame_bytes1 = bytearray(list(r1.readframes(r1.getnframes())))
frame_bytes2 = bytearray(list(r2.readframes(r2.getnframes())))

print(r1.getparams())

a = byte_xor(frame_bytes1,frame_bytes2)
#print(a)
#for i in range(len(frame_bytes1)):
#    tmp.append(bytes(frame_bytes1[i] ^ frame_bytes2[i]))
#    #print(flag)
#print(tmp)
#print(flag) 

f1 = wave.open('./otmp.wav', mode='wb') 
f1.setparams((2, 2, 48000, 230494, 'NONE', 'not compressed'))

f1.writeframes(a)

f1.close()


import PIL.Image as Image
import io
a = a.replace(b'\x00',b'')
print(len(a),a)
img = Image.open(io.BytesIO(a))
img.show
