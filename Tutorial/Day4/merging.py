import  cv2
import numpy as np

Image=cv2.imread('../../Assets/Card.jpg')
Horizantal=np.hstack((Image,Image))#For Horizantal Stacking
Vertical=np.vstack((Image,Image))#For Vertical Stacking

cv2.imshow("Horizantal",Horizantal)
cv2.imshow("Diagonal",Vertical)
cv2.waitKey(0)