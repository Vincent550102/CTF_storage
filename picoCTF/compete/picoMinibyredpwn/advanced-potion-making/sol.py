from PIL import Image
img = Image.open('advanced-potion-making.png')
width,height=img.size
print(img.mode)
main = (239, 18, 29)
for i in range(0,width):
    for j in range(0,height):
        tmp = img.getpixel((i,j))
        if tmp != main:
            img.putpixel((i,j),255)

img.show()
