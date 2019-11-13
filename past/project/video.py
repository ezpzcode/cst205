import numpy as np
import cv2
my_video = cv2.VideoCapture('missing.mp4')
frame_rate = my_video.get(cv2.CAP_PROP_FPS)
wait_value = int(1000/frame_rate)
while True:
 ret, frame = my_video.read()
 if ret:
 # CIE XYZ color space Recommendation BT.709 with D65 white point
 cie_xyz = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
 cv2.imshow('Missing Stapler', cie_xyz)
 cv2.waitKey(wait_value)
 else:
 break