import multiprocessing as mp
from math import floor
from PIL import Image
import sys


def convert_chunk(stream, content, chunk_num, chunk_size):
    content_len = len(content)
    content = content[chunk_num*chunk_size:(chunk_num+1)*chunk_size]
    colors, color = [], []
    tick = 0

    for i in content:
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
    stream.put((chunk_num, colors))


if __name__ =='__main__':
    mp.set_start_method('spawn')
    stream = mp.Queue()
    cores = 16
    with open(sys.argv[1], "rb") as file:
        content = file.read()
        content_len = len(content)
        chunk_size = floor(content_len/(4*(16-1)))*4

        chunk1 = mp.Process(target=convert_chunk, args=(stream, content, 0, chunk_size,)).start()
        chunk2 = mp.Process(target=convert_chunk, args=(stream, content, 1, chunk_size,)).start()
        chunk3 = mp.Process(target=convert_chunk, args=(stream, content, 2, chunk_size,)).start()
        chunk4 = mp.Process(target=convert_chunk, args=(stream, content, 3, chunk_size,)).start()
        chunk5 = mp.Process(target=convert_chunk, args=(stream, content, 4, chunk_size,)).start()
        chunk6 = mp.Process(target=convert_chunk, args=(stream, content, 5, chunk_size,)).start()
        chunk7 = mp.Process(target=convert_chunk, args=(stream, content, 6, chunk_size,)).start()
        chunk8 = mp.Process(target=convert_chunk, args=(stream, content, 7, chunk_size,)).start()
        chunk9 = mp.Process(target=convert_chunk, args=(stream, content, 8, chunk_size,)).start()
        chunk10 = mp.Process(target=convert_chunk, args=(stream, content, 9, chunk_size,)).start()
        chunk11 = mp.Process(target=convert_chunk, args=(stream, content, 10, chunk_size,)).start()
        chunk12 = mp.Process(target=convert_chunk, args=(stream, content, 11, chunk_size,)).start()
        chunk13 = mp.Process(target=convert_chunk, args=(stream, content, 12, chunk_size,)).start()
        chunk14 = mp.Process(target=convert_chunk, args=(stream, content, 13, chunk_size,)).start()
        chunk15 = mp.Process(target=convert_chunk, args=(stream, content, 14, chunk_size,)).start()
        chunk16 = mp.Process(target=convert_chunk, args=(stream, content, 15, chunk_size,)).start()

        uimgdata = []
        for q in range(16):
            uimgdata.append(stream.get())

        imgdata = []
        i, j = 0, 0
        while uimgdata != []:
            if uimgdata[j][0] == i:
                imgdata = imgdata + uimgdata[j][1]
                uimgdata.pop(j)
                j = 0
                i += 1
                continue
            j+=1

        tick = 0
        height, width = 0, 0

        while height * width < len(imgdata):
            if tick == 0:
                height += 1
                tick = 1
            else:
                width += 1
                tick = 0
        size = (height, width)

        img = Image.new("RGBA", size, "white")

        img.putdata(imgdata)
        img.save("test.png")
        #img.show()
