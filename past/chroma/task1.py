import numpy as np
from PIL import Image

im = Image.open('emil.jpg')
pixels = list(im.getdata())

print(max(pixels))