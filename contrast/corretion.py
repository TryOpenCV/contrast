import numpy as np
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

n = int(input('n: '))
image = Image.open("lenna.bmp")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        S = (a + b + c) // 3
        draw.point((i, j), (S, S, S))

image.save("ans.jpg", "JPEG")

image = Image.open("ans.jpg")
image.show()
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

im = Image.new("RGB", (width, height), "black")
draw = ImageDraw.Draw(im)
for i in range(width - 2):
    for j in range(height - 2):

        a1 = pix[i, j][0]
        b1 = pix[i, j][1]
        c1 = pix[i, j][2]
        mid1 = (a1 + b1 + c1) / 3

        a2 = pix[i, j + 1][0]
        b2 = pix[i, j + 1][1]
        c2 = pix[i, j + 1][2]
        mid2 = (a2 + b2 + c2) / 3

        a3 = pix[i, j + 2][0]
        b3 = pix[i, j + 2][1]
        c3 = pix[i, j + 2][2]
        mid3 = (a3 + b3 + c3) / 3

        a4 = pix[i + 1, j][0]
        b4 = pix[i + 1, j][1]
        c4 = pix[i + 1, j][2]
        mid4 = (a4 + b4 + c4) / 3

        a5 = pix[i + 1, j + 1][0]
        b5 = pix[i + 1, j + 1][1]
        c5 = pix[i + 1, j + 1][2]
        mid5 = (a5 + b5 + c5) / 3

        a6 = pix[i + 1, j + 2][0]
        b6 = pix[i + 1, j + 2][1]
        c6 = pix[i + 1, j + 2][2]
        mid6 = (a6 + b6 + c6) / 3

        a7 = pix[i + 2, j][0]
        b7 = pix[i + 2, j][1]
        c7 = pix[i + 2, j][2]
        mid7 = (a7 + b7 + c7) / 3

        a8 = pix[i + 2, j + 1][0]
        b8 = pix[i + 2, j + 1][1]
        c8 = pix[i + 2, j + 1][2]
        mid8 = (a8 + b8 + c8) / 3

        a9 = pix[i + 2, j + 2][0]
        b9 = pix[i + 2, j + 2][1]
        c9 = pix[i + 2, j + 2][2]
        mid9 = (a9 + b9 + c9) / 3

        zc = (mid1 + mid2 + mid3 + mid4 + mid6 + mid7 + mid8 + mid9) / 8
        z = mid5
        Cz = np.abs(z - zc) / z + zc
        Cz **= n

        if z < zc:
            z = zc * ((1 - Cz) / (1 + Cz))
        elif z > zc:
            z = zc * ((1 + Cz) / (1 - Cz))

        draw.point((i + 1, j + 1), (int(z), int(z), int(z)))

im.save("ans1.jpg", "JPEG")
im.show('After processing')

del draw