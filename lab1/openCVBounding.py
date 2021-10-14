#most boilerplate here borrowed from https://docs.opencv.org/master/dd/d49/tutorial_py_contour_features.html
#small bits borrowed from https://pythonprogramming.net/color-filter-python-opencv-tutorial/

import numpy as np
import cv2


cap = cv2.VideoCapture(0)

#upper and lower bounds for HSV "green," apparently hsv values in opencv range from 0 to 180

lower_green_hsv = np.array([30, 60, 30])
upper_green_hsv = np.array([90, 255, 255])


while(True):
    # Capture frame-by-frame
    
    _, frame = cap.read()

    # Our operations on the frame come here
    #convert to hsv to isolate green from the image
    transcodedFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Borrowed from https://pythonprogramming.net/color-filter-python-opencv-tutorial/
    thresh = cv2.inRange(transcodedFrame, lower_green_hsv, upper_green_hsv)

    # Display the resulting frame
    #ret,thresh = cv2.threshold(isolatedPixelData,170,255,cv2.THRESH_BINARY)
    contours,_ = cv2.findContours(thresh, 1, 2)
    #contours.sort(reverse=True, key=lambda x: cv2.contourArea(x)) #find the contour with the biggest area
    
    if contours: #contours may be empty sometimes, so we check, draw bounding box around contour around frame

        cnt = max(contours, key=cv2.contourArea) #find contour with the biggest area to draw
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(frame,[box],0,(0,0,255),2) #draw red bounding box in frame
        cv2.drawContours(thresh,[box],0,(255, 255, 255),2) #draw white bounding box here in the threshold image
    #draw frames
    cv2.imshow('frame',frame)
    cv2.imshow('rawThreshold',thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
