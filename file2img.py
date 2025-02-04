from PIL import Image
import sys

# read the file, and get all the bit values
with open(sys.argv[1], "rb") as file:
    colors, color = [], []
    tick = 0

    for i in file.read():
        if tick < 4:
            color.append(i)
            tick += 1
        else:
            colors.append(tuple(color))
            tick = 1
            color = []
            color.append(i)
    if len(color) > 0:
        while len(color) < 4:
            color.append(0)
        colors.append(tuple(color))

    tick = 0
    height, width = 0, 0

    while height * width < len(colors):
        if tick == 0:
            height += 1
            tick = 1
        else:
            width += 1
            tick = 0
    size = (height, width)

    img = Image.new("RGBA", size, "white")

    img.putdata(colors)
    img.save("test.png")
    #img.show()
