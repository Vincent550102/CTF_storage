from PIL import Image

img1 = Image.open('scrambled1.png')
img2 = Image.open('scrambled2.png')

img1.paste(img2)
img1.show()

img=img1
width,height=img.size
for i in range(0,width):
    for j in range(0,height):
        tmp=img.getpixel((i,j))
        print(tmp)
        if tmp[-1]%2==0:
            img.putpixel((i,j),0)
        else:
            img.putpixel((i,j),255)
#img.show()


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
