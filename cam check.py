
import cv2 as cv
import numpy as np
import cmapy

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    

    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    

    canny = cv.Canny(gray,100,100)
    cv.namedWindow("Cont",cv.WINDOW_NORMAL)
    cv.imshow("Cont",canny)    

    

    if cv.waitKey(1) == 27:
        break
