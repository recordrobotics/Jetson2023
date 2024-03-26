# Import
import robotpy_apriltag
from wpimath.geometry import Transform2d, Rotation2d, Translation2d
from estimate_pose import tagTransforms

# Sets up detector
detector = robotpy_apriltag.AprilTagDetector()
assert detector.addFamily("tag36h11")
config = robotpy_apriltag.AprilTagDetector.Config()
config.numThreads = 8
detector.setConfig(config)

# Sets up estimator
estimator = robotpy_apriltag.AprilTagPoseEstimator(
    robotpy_apriltag.AprilTagPoseEstimator.Config(
        0.1651*2,
        233.53139518,
        376.16494381,
        542.62032562,
        219.16328585,
    ))
    
def get_tags(frame, DETECTION_MARGIN_THRESHOLD = 40):
   tags = detector.detect(frame)
   filter_tags = [tag for tag in tags if 
                   tag.getDecisionMargin() > DETECTION_MARGIN_THRESHOLD and tag.getId() in tagTransforms.keys()]
   return filter_tags

# Function to detect tags
def detect_tag(frame, DETECTION_MARGIN_THRESHOLD = 40):
    '''
    Input: camera frame, decision margin threshold for apriltags
    Output: tag pose and tag_id
    '''

    # Gets all information about tag
    tags = detector.detect(frame)
    # Filters tags using a decision margin threshold and tag ID
    filter_tags = [tag for tag in tags if 
                   tag.getDecisionMargin() > DETECTION_MARGIN_THRESHOLD and tag.getId() in tagTransforms.keys()]

    #tag_poses = [(tag.getId(), estimator.estimateOrthogonalIteration(tag, 50).pose1) for tag in filter_tags]
    tag_poses = [(tag.getId(), estimator.estimateOrthogonalIteration(tag, 50)) for tag in filter_tags]
    #tag_poses.sort(key = lambda tuple: tuple[1].translation().dis)
    if len(tag_poses) > 0:
        # Gets first of filter_tags
        tag = tag_poses[0]
        # Gets tag ID
        tag_id = tag[0] # Gets ID
        # Gets tag pose
        tag_pose1 = tag[1].pose1
        tag_pose2 = tag[1].pose2

        # Figure out which one is right
        if tag_pose1.Z() > 0:
            tag_pose = tag_pose1
        elif tag_pose2.Z() > 0:
            tag_pose = tag_pose2
        else:
            tag_pose = tag_pose1
            print("both tag poses invalid")

        # Turns pose into a pose2d
        tag_pose_2d = Transform2d(Translation2d(tag_pose.X(), tag_pose.Z()), Rotation2d(tag_pose.rotation().Y()))

        # Printouts
        print("TRANSLATION: ", tag_pose.X(), tag_pose.Y(), tag_pose.Z())
        print("ROTATION: ", tag_pose.rotation().X(), tag_pose.rotation().Y(), tag_pose.rotation().Z())

        # Returns tag pose and ID
        return tag_pose_2d, tag_id
    return None, None