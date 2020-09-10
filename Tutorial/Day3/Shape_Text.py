import  cv2
import numpy as np

Custom_Image=np.zeros((1000,700))#Height and width of the image


'''In order to add
the color functionality'''

Custom_Image_1=np.zeros((500,500,3),np.uint8)
Custom_Image_1[:]=0,0,255 #For open cv it is BGR not RGB

print(Custom_Image_1)

cv2.imshow("Custom_Image",Custom_Image)
cv2.imshow("Custom_Image",Custom_Image_1) #Will display red colour
cv2.waitKey(0)