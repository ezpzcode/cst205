import numpy as np
import cv2

im_gray = cv2.imread('gogh.jpg', cv2.IMREAD_GRAYSCALE)
im_remap = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
cv2.imwrite("gogh_jet.jpg", im_remap)
