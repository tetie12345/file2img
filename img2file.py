from PIL import Image
import os, sys

img = Image.open(sys.argv[1])

pixels = img.load()

for i in img.height:
    for j in img.width:
        print(pixels[i,j])
