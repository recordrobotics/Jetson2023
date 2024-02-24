import robotpy_apriltag
from wpimath.geometry import Transform3d, Pose3d, Rotation3d, Pose2d, Rotation2d, Translation2d, Translation3d


tagTransforms = {
    6: Pose3d(Translation3d(1.8415, 8.2042, 1.355852), Rotation3d(0,0,4.71239))
}


def estimate_pose(robot_to_april, tag_id):
    april_to_robot = robot_to_april.inverse()
    global_to_april = tagTransforms[tag_id]
    global_to_robot = global_to_april.transformBy(april_to_robot)

    robotGlobalPose = Pose2d(Translation2d(global_to_robot.translation().X(), global_to_robot.translation().Y()),
                            Rotation2d(global_to_robot.rotation().Z()))
    
    return robotGlobalPose