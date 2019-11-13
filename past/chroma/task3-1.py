import numpy as np
from PIL import Image

im = Image.open('zebra.jpg')
pixels = list(im.getdata())

print(pixels)