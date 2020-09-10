import  cv2
import numpy as np


'''In order to add
the color functionality'''

Custom_Image_1=np.zeros((500,500,3),np.uint8)
'''
Function for drawing the line
1st=The file which is Custom_Image_1 for our case
2nd= Starting Point
3rd= Ending Point
4th=Color(red for our case)
5th= Thickness
'''
cv2.line(Custom_Image_1,(1,1),(Custom_Image_1.shape[1],Custom_Image_1.shape[0]),(0,0,255),3)
cv2.rectangle(Custom_Image_1,(0,0),(20,15),(255,0,0),cv2.FILLED)
cv2.circle(Custom_Image_1,(70,70),10,(0,255,0),7)
cv2.putText(Custom_Image_1,"Hello World",(400,400),cv2.FONT_ITALIC,0.5,(255,255,255),3)


print(Custom_Image_1)


cv2.imshow("Custom_Image",Custom_Image_1) #Will display red colour
cv2.waitKey(0)