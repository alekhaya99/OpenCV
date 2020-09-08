'''In order to read and
display the image'''
import cv2

image=cv2.imread('../../Assets/Test.jpeg')#Reads the image
cv2.imshow("Output",image) #Shows the image
cv2.waitKey(1000)#Adds delay to the showing of the image