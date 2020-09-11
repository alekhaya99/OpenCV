import cv2
import numpy as np

img=cv2.imread('../../Assets/Card.jpg')

width,height=250,350
Points_1=np.float32([[145,375],[222,375],[94,521],[179,529]])
Points_2=np.float32([[0,0],[width,0],[0,height],[width,height]])
Matrix=cv2.getPerspectiveTransform(Points_1,Points_2)
Image_Output=cv2.warpPerspective(img,Matrix,(width,height))

cv2.imshow('Modiffied Image',Image_Output)
cv2.waitKey(0)