import cv2

Video=cv2.VideoCapture(0)

Video.set(3,640)
Video.set(4,480)
Video.set(10,100)
while True:
    success,image=Video.read()
    cv2.imshow("Video" , image)
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break





