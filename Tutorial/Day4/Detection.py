import cv2

Image=cv2.imread('../../Assets/Test.jpeg')
#In order to detect an particular section in the image we need to convert it into HSV Format
HSV_Image=cv2.cvtColor(Image,cv2.COLOR_BGR2HSV)

cv2.imshow('Original Image',Image)
cv2.imshow("Modified_Image",HSV_Image)
cv2.waitKey(0)