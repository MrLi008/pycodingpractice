# coding=utf8


from PIL import Image
import math



urlImg = 'lena.bmp'

img = Image.open(urlImg)

# img.show()

v = img.split()
#
# for _v in v:
#     _v.show()

img2 = img.resize((img.width/2, img.height/2))
# img2.show()

width = img.width if img.width>img.height else img.height
img2 = img.rotate(45)
img2 = img2.resize((int(width*math.sqrt(2)), int(width*math.sqrt(2))))
img2.show()


def hideInfoInImage(img, info):
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    if info.mode != 'L' and info.mode != '1':
        info = info.convert('L')

    print img.mode,' ', info.mode

    img.putalpha(info)

    return img

img_hide = Image.open('lena.bmp')

img_main = Image.open('tt3.bmp')
img_main = img_main.resize((img_hide.width, img_hide.height))
img_res = hideInfoInImage(img_main, img_hide)
img_res.show()
for n in img_res.split():
    n.show()
