from PIL import Image
import numpy as np
import imageio as im
dataI = Image.open("I.png")
dataE = Image.open("E.png")
dataEprime = Image.open("Eprime.png")
datakey1 = Image.open("key1.png")
datakey2 = Image.open("key2.png")

data = np.zeros((120000,3),int)
e = np.zeros((120000), int)
w, h = datakey1.size
for i in range(h):
    for j in range(w):
        data[i*400+j][0] = datakey1.getpixel((j,i))
        data[i*400+j][1] = datakey2.getpixel((j,i))
        data[i*400+j][2] = dataI.getpixel((j,i))
        e[i*400+j] = dataEprime.getpixel((j,i))

