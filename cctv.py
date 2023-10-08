import cv2
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, from1 = cam.read()
    ret, from2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    if cv2.waitKey(10) == ord('p'):
        break
    cv2.imshow('vasu cam', diff)