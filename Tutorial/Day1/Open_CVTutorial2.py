import cv2

Video=cv2.VideoCapture('../../Assets/Test_Video.mp4')

while True:
    success,image=Video.read()
    cv2.imshow("Video" , image)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

