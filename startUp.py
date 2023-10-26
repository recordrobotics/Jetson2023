import numpy as np
import cv2 as cv
import logging
import math
import time
from pupil_apriltags import Detector
from pupil_apriltags import draw_tags

cap = cv.VideoCapture(0)

at_detector = Detector(
    families="tag36h11",
    nthreads=1,
    quad_decimate=1.0,
    quad_sigma=0.0,
    refine_edges=1,
    decode_sharpening=0.25,
    debug=0
)

while(True):
    start_time = time.time()
    # image
    ret, frame = cap.read()

    # display color
    cv.imshow('frame',ret)

    # detect apriltags
    tags = at_detector.detect(
            cv.cvtColor(frame, cv.COLOR_BGR2GRAY),
            estimate_tag_pose=True,
            camera_params=None,
            tag_size=8*0.0254,
        )
    
    # draw apriltag locations
    debug_image = draw_tags(debug_image, tags, time.time() - start_time)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    # display colorless image with apriltags marked
    cv.imshow('AprilTag Detect Demo', debug_image)

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

def draw_tags(
    image,
    tags,
    elapsed_time,
):
    for tag in tags:
        tag_family = tag.tag_family
        tag_id = tag.tag_id
        center = tag.center
        corners = tag.corners

        center = (int(center[0]), int(center[1]))
        corner_01 = (int(corners[0][0]), int(corners[0][1]))
        corner_02 = (int(corners[1][0]), int(corners[1][1]))
        corner_03 = (int(corners[2][0]), int(corners[2][1]))
        corner_04 = (int(corners[3][0]), int(corners[3][1]))

        # center
        cv.circle(image, (center[0], center[1]), 5, (0, 0, 255), 2)

        # sides
        cv.line(image, (corner_01[0], corner_01[1]),
                (corner_02[0], corner_02[1]), (255, 0, 0), 2)
        cv.line(image, (corner_02[0], corner_02[1]),
                (corner_03[0], corner_03[1]), (255, 0, 0), 2)
        cv.line(image, (corner_03[0], corner_03[1]),
                (corner_04[0], corner_04[1]), (0, 255, 0), 2)
        cv.line(image, (corner_04[0], corner_04[1]),
                (corner_01[0], corner_01[1]), (0, 255, 0), 2)

       # tag name
        cv.putText(image, str(tag_id), (center[0] - 10, center[1] - 10),
                   cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2, cv.LINE_AA)

    # processing time
    cv.putText(image,
               "Elapsed Time:" + '{:.1f}'.format(elapsed_time * 1000) + "ms",
               (10, 30), cv.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2,
               cv.LINE_AA)

    return image