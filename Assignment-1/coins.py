import cv2
import numpy as np

img = cv2.imread("images/coins.png",1)

img = cv2.convertScaleAbs(img, 1, 0.5)

#original
cv2.imshow('original image',img)

#grey scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#binary scale
thresh, binary = cv2.threshold(gray,71,255, cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)
cv2.imshow('binary image', binary)
cv2.waitKey()
cv2.destroyAllWindows()

img = cv2.connectedComponents(binary)
print("Total Objects: ",img[0]-1)
