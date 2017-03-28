# coding=utf8

from PIL import Image
import math



img = Image.open('tt3.bmp')
img.show()
img = img.convert('HSV')
img.show()
v = img.split()

for _v in v:


    _v.show()






