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
from detect_tags import detect_tags, filter_tags
from draw_tags import draw_tags
from estimate_pose import estimate_pose, is_tag_valid, convert_for_export, get_xyz

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
        tags = detect_tags(frame)
        filtered_tags = filter_tags(tags)

        if len(filtered_tags) > 0 and is_tag_valid(tag=filtered_tags[0]):
            # Gets pose
            global_to_robot = estimate_pose(filtered_tags[0])
            pose = convert_for_export(global_to_robot)
            #(X,Y,Z) = get_xyz(global_to_robot)
            #put_pose([[X,Y,Z]])
            put_pose(pose)
            put_tag_id(filtered_tags[0].tag_id)
            put_has_pose(True)
        #draw_tags(frame, filtered_tags, time.time() - start_time)
        #start_time = time.time()
        #cv.imshow('image', frame)
        #if cv.waitKey(1) & 0xFF == ord('q'):
        #    break
        else:
            put_has_pose(False)


# When everything done, release the capture
cam.release()
cv.destroyAllWindows()
