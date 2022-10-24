import cv2 as cv
import numpy as np
import time
import imutils


cam = cv.VideoCapture(0)
time.sleep(1)

firstFrame = None
area = 500

while True:
    _,img = cam.read()
    text = "Normal"
    img = imutils.resize(img,width=500)
    grayImg = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gaussianImg = cv.GaussianBlur(grayImg,(21,21),0)
    if firstFrame is None:
        firstFrame = gaussianImg
        continue
    imgDiff = cv.absdiff(firstFrame,gaussianImg)
    thresImg = cv.threshold(imgDiff,25,255,cv.THRESH_BINARY)[1]
    thresImg = cv.dilate(thresImg,None,iterations=2)
    cnts = cv.findContours(thresImg.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    for c in cnts:
        if(cv.contourArea(c)<area):
            continue
        (x,y,w,h) = cv.boundingRect(c)
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text = "Moving object detected"
    cv.putText(img,text,(10,20),cv.FONT_HERSHEY_SCRIPT_SIMPLEX,0.5,(0,255,0),2)
    cv.imshow("CameraFeed",img)
    if(cv.waitKey()==ord('q')):
        break


cam.release()
cv.destroyAllWindows()
