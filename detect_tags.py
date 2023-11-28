# Imports
import numpy as np
import cv2 as cv
#import networktables
import logging
import math
import time
from pupil_apriltags import Detector


# Creates a detector object from pupil_apriltags
at_detector = Detector(
    families="tag16h5",
    nthreads=1,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=1,
    decode_sharpening=0.25,
    debug=0
)


# Function that takes in a camera frame and returns tag data
#def detect_tags(frame, camera_params = [862.80475869, 850.06137657, 533.8004744, 423.2742388]):
def detect_tags(frame, camera_params = [850.06137657, 862.80475869, 423.2742388, 533.8004744]):
#def detect_tags(frame, camera_params = [862.80475869, 850.06137657, 533.8004744, 423.2742388]):


    # Gets all detected apriltags
    tags = at_detector.detect(
            cv.cvtColor(frame, cv.COLOR_BGR2GRAY),
            estimate_tag_pose=True,
            camera_params=camera_params,
            tag_size=6*0.0254,
        )
    # Returns
    return tags


# Function that takes in a "tags" object and returns only the tags that the camera is confident in
def filter_tags(tags, DECISION_MARGIN_THRESHOLD = 40):
    # Gets a list
    filtered_tags = [tag for tag in tags if tag.decision_margin > DECISION_MARGIN_THRESHOLD]
    # Returns filtered tags
    return filtered_tags



if __name__ == "__main__":

    # Opens opencv video capture object
    cap = cv.VideoCapture(1)

    while(True):
        # Imports
        from draw_tags import draw_tags
        from networktables import NetworkTables
        start_time = time.time()

        # Gets frame
        ret, frame = cap.read()

        # display color
        cv.imshow('frame',frame)

        # Detects tags
        tags = detect_tags(frame)
        filtered_tags = filter_tags(tags)
    
        # draw apriltag locations
        debug_image = draw_tags(frame, tags, time.time() - start_time)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        cv.imshow('AprilTag Detect Demo', debug_image)
        
        # send values to networktables
        #networktables(tags)
        
        
        
        
        

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()