from PIL import Image,ImageEnhance

img1 = Image.open('scrambled1.png')
img2 = Image.open('scrambled2.png')

#img1.paste(img2)
#img2.show()

    
img = Image.blend(img2, img1, 0.5)

enh_con = ImageEnhance.Contrast(img)
contrast = 1005
image_contrasted = enh_con.enhance(contrast)
image_contrasted.save('flag.png')
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
