# Imports
print("numpy")
import numpy as np
print("cv")
import cv2 as cv
print("after cv")

# Opens opencv video capture object
print("Opening VideoCapture")
cam = cv.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=960, height=540 ! nvvidconv ! video/x-raw,format=GRAY8 ! videoconvert ! video/x-raw,format=GRAY8 ! appsink")
#last_time = time.time()

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

directory = "calibration/calibration_images"
counter=1

while True:
    # Gets frame
    ret, frame = cam.read()
    if not frame is None:
        #ret,corners=cv.findChessboardCorners(frame, (7,6), None)
        #if ret == True:
        #    corners2 = cv.cornerSubPix(frame, corners, (11,11), (-1,-1), criteria)
        #    cv.drawChessboardCorners(frame, (7,6), corners2, ret)
        cv.imshow('image', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            filename = directory+"/image_"+str(counter)+".jpg"
            cv.imwrite(filename, frame)
            counter+=1
            print("PICTURE TAKEN (file at "+filename+")")

# When everything done, release the capture
cam.release()
cv.destroyAllWindows()
