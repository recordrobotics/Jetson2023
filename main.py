import time
#time.sleep(60) # zzzzzzz

# Imports
import cv2 as cv
from client_networktables import initialize_networktables, put_pose, put_has_pose, put_tag_id

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

    # If a frame exists
    if not frame is None:
        # Detects tags
        robot_to_april, tag_id = detect_tag(frame=frame)
        
        # If a tag exists:
        if robot_to_april:
            # Gets pose
            pose3d = estimate_pose(robot_to_april, tag_id)
            pose = [pose3d.translation().X(), pose3d.translation().Y(), pose3d.rotation().Z()]
            # Puts on networktables
            put_pose(pose)
            put_tag_id(tag_id)
            put_has_pose(True)
        else:
            put_has_pose(False)


# When everything done, release the capture
cam.release()
cv.destroyAllWindows()
