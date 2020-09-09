'''In order to read and
display the image'''
import cv2

image=cv2.imread('../../Assets/Test.jpeg')#Reads the image
print(image.shape) #In order to check the size of the image

Image_Resize=cv2.resize(image,(300,200))#In order to resize the image

Cropped_Image=image[100:500,500:1000]#For cropping height comes first and then the width

cv2.imshow("Output",image) #Shows the image
cv2.imshow("Resized Image",Image_Resize)
cv2.imshow("Cropped Image",Cropped_Image)
cv2.waitKey(0)#Adds delay to the showing