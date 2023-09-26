import cv2
import numpy as np

img = cv2.imread("./images/image.jpg",1)

#original
h,w,c = img.shape
print("Original Height and Width:", h,"x", w)
#427 x 640
cv2.imshow('original image',img)
cv2.waitKey()
cv2.destroyAllWindows() 

#resizing
resized_img = cv2.resize(img, ( 256,256 ) , interpolation = cv2.INTER_LINEAR)  
rh,rw,rc = resized_img.shape
print("Resized Height and Width:", rh,"x", rw)
# 256 x 256
cv2.imshow('resized image', resized_img)
cv2.waitKey()
cv2.destroyAllWindows() 

#grey scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
combined_image = np.hstack((img,cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)))
cv2.imshow('Gray image', combined_image)
cv2.waitKey()
cv2.destroyAllWindows()

#binary scale
binary = cv2.threshold(gray,128,255, cv2.THRESH_BINARY)
combined_image = np.hstack((img, cv2.cvtColor(binary[1], cv2.COLOR_GRAY2BGR)))
cv2.imshow('binary image', combined_image)
cv2.waitKey()
cv2.destroyAllWindows()