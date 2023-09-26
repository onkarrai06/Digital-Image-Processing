import cv2
import numpy as np

img = cv2.imread("images/coins.png",1)

#original
cv2.imshow('original image',img)

#grey scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#binary scale
thresh, binary = cv2.threshold(gray,140,255, cv2.THRESH_BINARY)

binary = cv2.bitwise_not(binary)
result_image = cv2.bitwise_and(img, img, mask=binary)

#counting objects
count, _ = cv2.connectedComponents(binary)


result_image = cv2.putText(result_image, "Total Objects: "+str(count-1), (200,50), cv2.FONT_HERSHEY_TRIPLEX, 1, (255,255,255), 1)

cv2.imshow("Binary Image", binary)
cv2.imshow('Final segmented Image', result_image)
cv2.waitKey()
cv2.destroyAllWindows()

print("Total Objects: ",count-1)
