'''
from PIL import Image
img = Image.open('./encoded.png')
width,height=img.size
for i in range(0,width):
    for j in range(0,height):
        tmp = img.getpixel((i,j))
        #print(tmp)
        npix = ((tmp[0]-245+255)%255,(tmp[1]-190+255)%255,(tmp[2]-40+255)%255)
        img.putpixel((i,j),npix)
img.show()
'''
'''
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open('encoded.png')
data = np.array(img)
extracted = (data[...,0] ^ data[...,1] ^ data[...,2]) & 0x111111111111111
plt.imshow(extracted)
plt.show()
'''

#!/usr/bin/env python3
from PIL import Image, ImageColor
import qrcode
qr_img = qrcode.make('Secret')
qr_pixels = qr_img.load()
img = Image.open('image.png')
for i in range(qr_img.size[0]):
    for j in range(qr_img.size[1]):
    pixel = img.getpixel((i, j))
    pixel = (pixel[0], (pixel[1] & 0b11111110) | int(qr_pixels[i, j] == 255), pixel[2])
    img.putpixel((i, j), pixel)
img.save('qr-hidden.png')
