import numpy as np
import cv2 as cv
#import networktables
import logging
import math
import time
from pupil_apriltags import Detector
from draw_tags import draw_tags

cap = cv.VideoCapture(1)

at_detector = Detector(
    families="tag16h5",
    nthreads=1,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=1,
    decode_sharpening=0.25,
    debug=0
)

#vision_nt = networktables.getTable('Vision')
# waiting for networktables
time.sleep(0.5)

while(True):
    start_time = time.time()
    # image
    ret, frame = cap.read()

    # display color
    cv.imshow('frame',frame)

    camera_params = [862.80475869, 850.06137657, 533.8004744, 423.2742388]
    #camera_params = [533.8004744, 423.2742388, 862.80475869, 850.06137657]
    #camera_params = [862.80475869, 533.8004744, 850.06137657, 423.2742388]

    # detect apriltags
    tags = at_detector.detect(
            cv.cvtColor(frame, cv.COLOR_BGR2GRAY),
            estimate_tag_pose=True,
            camera_params=camera_params,
            tag_size=8*0.0254,
        )
    
    #print(tags)
    
    if len(tags) > 0:
        for tag in tags:
            if tag.decision_margin > 40:
                print(f"{tag.tag_id}, Margin: {tag.decision_margin}")

    # draw apriltag locations
    debug_image = draw_tags(frame, tags, time.time() - start_time)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    # sending pose
    #vision_nt.putNumberArray('target_position', tags.pose_t)  
    
    # display colorless image with apriltags marked
    cv.imshow('AprilTag Detect Demo', debug_image)

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()