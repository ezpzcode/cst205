import numpy as np
import cv2

img = cv2.imread('마약왕.jpg', cv2.IMREAD_GRAYSCALE)
img_remap = cv2.applyColorMap(img, cv2.COLORMAP_JET)

cv2.imshow("ma in Gray", img_remap)
cv2.waitKey()


