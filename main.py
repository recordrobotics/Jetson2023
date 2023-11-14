# Imports
import numpy as np
import cv2 as cv
#import networktables
import logging
import math
import time
from pupil_apriltags import Detector
# Python imports
from detect_tags import detect_tags, filter_tags
from draw_tags import draw_tags


# Opens opencv video capture object
cap = cv.VideoCapture(1)
start_time = time.time()


while(True):
    # Gets frame
    ret, frame = cap.read()

    # Detects tags
    tags = detect_tags(frame)
    filtered_tags = filter_tags(tags)
    
    # draw apriltag locations
    debug_image = draw_tags(frame, filtered_tags, time.time() - start_time)

    # display drawn tag
    cv.imshow('frame', debug_image)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()