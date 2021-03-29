from PIL import Image
import numpy as np
def vstack(images):
    if len(images) == 0:
        raise ValueError("Need 0 or more images")

    if isinstance(images[0], np.ndarray):
        images = [Image.fromarray(img) for img in images]
    width = max([img.size[0] for img in images])
    height = sum([img.size[1] for img in images])
    stacked = Image.new(images[0].mode, (width, height))

    y_pos = 0
    for img in images:
        stacked.paste(img, (0, y_pos))
        y_pos += img.size[1]
    return stacked


def hstack(images):
    if len(images) == 0:
        raise ValueError("Need 0 or more images")

    if isinstance(images[0], np.ndarray):
        images = [Image.fromarray(img) for img in images]
    width = sum([img.size[0] for img in images])
    height = max([img.size[1] for img in images])
    stacked = Image.new(images[0].mode, (width, height))

    x_pos = 0
    for img in images:
        stacked.paste(img, (x_pos, 0))
        x_pos += img.size[0]
    return stacked

img1 = Image.open('scrambled1.png')
img2 = Image.open('scrambled2.png')

#img1.paste(img2)
#img2.show()

    
img = Image.blend(img1, img2, 0.5)
img.show()
img.save('new.png')
'''
lena = img1
pixsels = lena.load()
width=lena.size[0]
height=lena.size[1]
list1=[]
for x in range(0,width):
  for y in range(0,height):
    r,g,b=pixsels[x,y]
    if r==255 and g==255:
      pass
    else:
      if int(bin(b)[-1])==1:
        list1.append(0)
      else:
        list1.append(1)
print (len(list1))
im=Image.new("1",(300,300))
i=0
while i<len(list1):
   im.putpixel((i%300,i//300),list1[i])
   i=i+1
im.show()
'''
