# Imports
import cv2 as cv

# Python imports
from detect_tags import detect_tag
from estimate_pose import estimate_pose

# Opens opencv video capture object
print("Opening VideoCapture")
cam = cv.VideoCapture(0)

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
            print(pose)

    else:
        print("none")
        

# When everything done, release the capture
cam.release()
cv.destroyAllWindows()