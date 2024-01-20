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
from estimate_pose_test import estimate_pose, is_tag_valid, get_xyz


# Opens opencv video capture object
cap = cv.VideoCapture(1)
start_time = time.time()


# Draws
from matplotlib import pyplot as plt
import pygame

pygame.init()
size = width, height = 20*40, 20*40
screen = pygame.display.set_mode(size)
position=[0,0]
white=[255,255,255]

    
while(True):

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

        #print(filtered_tags)

        translation = filtered_tags[0].pose_t

        #print(translation[0][0], translation[1][0], translation[2][0])

        
        # Gets pose
        #global_to_camera = estimate_pose(filtered_tags[0])
        #X, Y, Z = get_xyz(global_to_camera)

        X, Y, Z = translation[0][0], translation[1][0], translation[2][0]

        position[0] = Y*300 + 400
        position[1] = Z*300 + 400

        print(str(X)[:5], str(Y)[:5], str(Z)[:5])
                    
        screen.fill(white)

        pygame.draw.circle(screen,[255,0,0],position,5,5)
        pygame.display.flip()
        

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()