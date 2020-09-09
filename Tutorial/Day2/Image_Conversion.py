import cv2
import numpy as np

Image=cv2.imread('../../Assets/Test.jpeg')
kernel=np.ones((5,5),np.uint8)#kernel matrix


Grey_Scale_Image=cv2.cvtColor(Image,cv2.COLOR_BGR2GRAY)
Blur_image=cv2.GaussianBlur(Grey_Scale_Image,(5,7),0) #Always will be odd numbers
Canny_Image=cv2.Canny(Image,150,200) #Thresold value
Image_Dilation=cv2.dilate(Canny_Image,kernel,iterations=8)#Iteration defines the thickness
Image_Dilation1=cv2.dilate(Canny_Image,kernel,iterations=1)
Image_Eroded=cv2.erode(Canny_Image,kernel,iterations=1)

cv2.imshow("Gray Image",Grey_Scale_Image)
cv2.imshow('Blur Image',Blur_image)
cv2.imshow('Canny Image',Canny_Image)
cv2.imshow('Dilated Image',Image_Dilation)
cv2.imshow('Dilated Image1',Image_Dilation1)
cv2.imshow('Eroded Image',Image_Eroded)
cv2.imshow('Original Image',Image)
cv2.waitKey(0)
