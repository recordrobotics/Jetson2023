# Imports
import numpy as np
import cv2 as cv
#import networktables
import logging
import math
import time
from pupil_apriltags import Detector
import matplotlib
import pylab as plt
# Python imports
from detect_tags import detect_tags, filter_tags
from draw_tags import draw_tags
from estimate_pose import estimate_pose, is_tag_valid


# Opens opencv video capture object
cap = cv.VideoCapture(1)
start_time = time.time()


# Draws
from matplotlib import pyplot as plt
import pygame

pygame.init()
size = width, height = 16*40, 10*40
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

        # Estimates pose
        global_to_camera = estimate_pose(filtered_tags[0])

        # Pygame DRAW
        X = global_to_camera[0,3]
        Y = global_to_camera[1,3]

        position[0] = X*40
        position[1] = Y*40
                    
        screen.fill(white)

        pygame.draw.circle(screen,[255,0,0],position,5,5)
        pygame.display.flip()

    if cv.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()