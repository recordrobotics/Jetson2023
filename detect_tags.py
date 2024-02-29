# Import
import cv2
import robotpy_apriltag_download as robotpy_apriltag
from estimate_pose import tagTransforms

# Sets up detector
detector = robotpy_apriltag.AprilTagDetector()
assert detector.addFamily("tag36h11")

# Sets up estimator
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
    '''
    Input: camera frame, decision margin threshold for apriltags
    Output: tag pose and tag_id
    '''
    # Turns tag to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gets all information about tag
    tags = detector.detect(gray)

    # Filters tags using a decision margin threshold and tag ID
    filter_tags = [tag for tag in tags if 
                   tag.getDecisionMargin() > DETECTION_MARGIN_THRESHOLD and tag.getId in tagTransforms.keys()]

    if len(filter_tags) > 0:
        # Gets first of filter_tags
        tag = filter_tags[0]
        # Gets tag ID
        tag_id = tag.getId() # Gets ID
        # Gets tag pose
        tag_pose = estimator.estimateOrthogonalIteration(tag, 50).pose1
        # Returns tag pose and ID
        return tag_pose, tag_id
    return None, None