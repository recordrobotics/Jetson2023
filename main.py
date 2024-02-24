import time
#time.sleep(60) # zzzzzzz

# Imports
print("numpy")
import numpy as np
print("cv")
import cv2 as cv
print("after cv")
from client_networktables import initialize_networktables, put_pose, put_has_pose, put_tag_id
import logging
import math
from pupil_apriltags import Detector

# Python imports
from detect_tags import detect_tag
from estimate_pose import estimate_pose

# Initialize networktables
print("Initializing networktables")
initialize_networktables("10.67.31.2") # 10.TE.AM.2

# Opens opencv video capture object
print("Opening VideoCapture")
cam = cv.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=960, height=540 ! nvvidconv ! video/x-raw,format=GRAY8 ! videoconvert ! video/x-raw,format=GRAY8 ! appsink")
start_time = time.time()

while True:

    # Gets frame
    ret, frame = cam.read()
    if not frame is None:
        # Detects tags

        robot_to_april, tag_id = detect_tag(frame=frame)
        
        if robot_to_april:
            # Gets pose
            pose = estimate_pose(robot_to_april, tag_id)
            pose = [pose.translation().X(), pose.translation().Y(), pose.rotation().Z()]
            put_pose(pose)
            put_tag_id(tag_id)
            put_has_pose(True)
        else:
            put_has_pose(False)


# When everything done, release the capture
cam.release()
cv.destroyAllWindows()
