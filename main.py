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
from estimate_pose import estimate_pose, is_tag_valid, get_xyz

# Opens opencv video capture object
#cap = cv.VideoCapture(1)
cap = cv.VideoCapture(0, cv.CAP_DSHOW) # this is the magic!
cap.set(cv.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 720)
start_time = time.time()


# Draws
from matplotlib import pyplot as plt
import pygame

pygame.init()
size = width, height = 13.7986 * 100, 8.2106*100
screen = pygame.display.set_mode(size)
position=[0,0]
white=[255,255,255]

    
while True:

    # Gets frame
    ret, frame = cap.read()

    # Detects tags
    tags = detect_tags(frame)
    filtered_tags = filter_tags(tags)
    
    # draw apriltag locations
    filtered_image = draw_tags(frame, filtered_tags, time.time() - start_time)
    cv.imshow('frame', filtered_image) # Puts on opencv display

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop=False

    if len(filtered_tags) > 0 and is_tag_valid(tag=filtered_tags[0]):


        translation = filtered_tags[0].pose_t

        #print(translation[0][0], translation[1][0], translation[2][0])

        
        # Gets pose
        global_to_robot = estimate_pose(filtered_tags[0])
        #X, Y, Z = get_xyz(global_to_robot)


        X, Y, Z = translation[0][0], translation[1][0], translation[2][0]
        print(str(X)[:6], str(Y)[:6], str(Z)[:6])#                             UNCOMMENT FOR TRANSLATION
        #print(global_to_robot)

        position[0] = Z*100
        position[1] = X*100

        screen.fill(white)

        pygame.draw.circle(screen,[255,0,0],position,10,10)
        pygame.display.flip()
        

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()