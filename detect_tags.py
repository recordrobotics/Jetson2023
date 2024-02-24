# Imports
import cv2 as cv
#import networktables
import time
from pupil_apriltags import Detector
import cv2
import robotpy_apriltag

# Sets up detector
detector = robotpy_apriltag.AprilTagDetector()
assert detector.addFamily("tag36h11")
estimator = robotpy_apriltag.AprilTagPoseEstimator(
    robotpy_apriltag.AprilTagPoseEstimator.Config(
        0.1651,
        483.481,
        479.381,
        512.579,
        297.779,
    ))


# Function to detect tags
def detect_tag(frame, DETECTION_MARGIN_THRESHOLD = 40):
    # Turns tag to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Filters tags using a decision margin threshold
    tag_info = detector.detect(gray)

    filter_tags = [tag for tag in tag_info if tag.getDecisionMargin() > DETECTION_MARGIN_THRESHOLD]

    if len(filter_tags) > 0:
        tag = filter_tags[0]
        tag_id = tag.getId() # Gets ID
        tag_pose = estimator.estimateOrthogonalIteration(tag, 50).pose1 # Gets pose
        return tag_pose, tag_id
    return None, None