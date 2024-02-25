# Imports
from wpimath.geometry import Transform3d, Pose3d, Rotation3d, Pose2d, Rotation2d, Translation2d, Translation3d
from wpimath.units import degreesToRadians, inchesToMeters
import csv

with open('tag_poses', mode='r') as infile:
    reader = csv.reader(infile, delimiter=" ")
    headers = next(reader) # skips header line
    # Gets dict of all tag transforms
    tagTransforms = {
        int(rows[0]):
        Pose3d(
            Translation3d(
                x = inchesToMeters(float(rows[1])), 
                y = inchesToMeters(float(rows[2])), 
                z = inchesToMeters(float(rows[3])), 
            ),
            Rotation3d(
                pitch = 0,
                roll = 0,
                yaw = degreesToRadians(float(rows[4][:-1]))
            ),
        )
        for rows in reader
    }


# Camera to robot translation
camera_to_robot = Transform3d(Translation3d(), Rotation3d())


def estimate_pose(camera_to_april, tag_id):
    '''
    Input: robot to apriltag transform and the ID of the apriltag detected
    Output: robot's global pose
    '''
    global_to_april = tagTransforms[tag_id]
    april_to_camera = camera_to_april.inverse()
    global_to_robot = global_to_april.transformBy(april_to_camera).transformBy(camera_to_robot)

    # Converts Pose3d to Pose2d then returns
    robotGlobalPose = global_to_robot.toPose2d()
    return robotGlobalPose