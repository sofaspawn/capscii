#! /usr/bin/env python3

from PIL import Image
im = Image.open("geto.jpeg")
print(im.format, im.size, im.mode)
