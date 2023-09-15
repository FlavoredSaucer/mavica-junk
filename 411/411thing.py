
from PIL import Image
import numpy as np

width = 64
height = 48

im = open("A:/MVC-001F.411","r+b")

imlist = list(im.read())

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

Luma = []
Cb = []
Cr = []

for i in range(int((width/4)*height)):
    li = i*6
    for x in range(4):
        Luma.append(imlist[li+x])
        Cb.append(imlist[li+4])
        Cr.append(imlist[li+5])

dlist = np.ndarray((height,width,3),dtype="uint8")

for y in range(height):
    ly = y*width
    for x in range(width):
        Y = Luma[ly+x] - 16
        U = Cb[ly+x] - 128
        V = Cr[ly+x] - 128
        dlist[y][x][0] = clamp(int((298.082*Y/256) + (408.583*V/256)), 0, 255)
        dlist[y][x][1] = clamp(int((298.082*Y/256) - (100.291*U/256) - (208.120*V/256)), 0, 255)
        dlist[y][x][2] = clamp(int((298.082*Y/256) + (516.412*U/256)), 0, 255)

# for y in range(height):
#     ly = y*width
#     for x in range(width):
#         dlist[y][x][0] = Luma[ly+x]
#         dlist[y][x][1] = Cb[ly+x]
#         dlist[y][x][2] = Cr[ly+x]




print(dlist)

templuma = np.reshape(dlist,(height,width,3))

# image = Image.fromarray(templuma,mode="YCbCr").convert("RGB")

image = Image.fromarray(templuma,mode="RGB")

image.save("asd1.png")