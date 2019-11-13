from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
import numpy as np
import cv2

# grab the image URL
html = urlopen('https://www.britannica.com/topic/The-Starry-Night')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
li = []
for image in images: 
    li.append(image['src'])
print(li)

# grab the image data
for i in li:
	r = urlopen(i)
	image = np.asarray(bytearray(r.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	print(image)