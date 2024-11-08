from PIL import Image
import os, sys

img = Image.open(sys.argv[1])

width, height = img.size

pixels = img.load()

print(width, height, img.size)
with open("test.txt", "w") as file:
    for i in range(height):
        for j in range(width):
            file.write(f"{chr(pixels[j,i][0])}{chr(pixels[j,i][1])}{chr(pixels[j,i][2])}{chr(pixels[j,i][3])}")
