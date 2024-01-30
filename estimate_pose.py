# Imports
import math
import numpy as np
from scipy.spatial.transform import Rotation



def get_transformation_matrix(rotation_matrix, translation_matrix):
    '''
    Input: rotation & translation matrix
    Output: transformation matrix
    '''

    # Creates a matrix that is a concatenated rotation next to translation
    n1 = np.concatenate((rotation_matrix, translation_matrix), axis=1)

    # Adds horizonal array of 0's below the existing matrix
    horizontal_array = np.array([[0,0,0,1]])
    n2 = np.concatenate((n1, horizontal_array), axis=0)

    # Returns
    return n2


# Rotation matrix that does nothing
no_rotation = np.array([[1,0,0],
                        [0,1,0],
                        [0,0,1]])

# Rotation matrix that rotates around y by 180 degrees
rotation_by_180d = np.array([[-1,0,0],
                            [0,1,0],
                            [0,0,-1]])

# Rotation matrix that rotates around y by 120 degrees
rotation_by_120d = np.array([[ -0.5,  0,  0.8660254],
                             [0,  1.,  0],
                             [-0.8660254,  0, -0.5]])

# Rotation matrix that rotates around y by 270 degrees
rotation_by_270d = np.array([[0, 0, -1],
                             [0, 1, 0],
                             [1, 0, 0]])

# Rotation matrix that rotates around y by 60 degrees
rotation_by_60d = np.array([[0.5, 0, 0.8660254],
                            [0, 1, 0],
                            [-0.8660254, 0, 0.5]])

# Rotation matrix that rotates around y by 300 degrees
rotation_by_300d = np.array([[0.5, 0, -0.8660254],
                             [0, 1, 0],
                             [0.8660254, 0, 0.5]])

# Rotation matrix that rotates around y by 240 degrees
rotation_by_240d = np.array([[-0.5, 0, -0.8660254],
                             [0, 1, 0],
                             [0.8660254, 0, -0.5]])

# Rotation matrix for flipping z
flip_z = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, -1]])

# Rotation matrix for flipping x
flip_x = np.array([[-1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]])

# Rotation matrix for rotating around y by 90 degrees
rotation_by_90d = np.array([[0, 0, 1],
                            [0, 1, 0],
                            [-1, 0, 0]])

# Transformation matrix for flipping z
flip_z_transform = get_transformation_matrix(flip_z, np.array([[0, 0, 0]]).T)


'''
All distances are in meters.
The algebra below looks questionable, but that is because some adjustments were necessary to take into account the strange tag frame
z is flipped because the z axis in the tag frame is INTO the tag
To place the origin in the top left, the x coordinate of tag 6 was taken as the x coordinate of the origin
orientations of the tags in the original frame were subtracted from 360 degrees to get their orientation in the flipped frame
'''
global_to_tag_transformations = {
    1: get_transformation_matrix(rotation_by_240d, np.array([[8.2042 - 0.2459, 1.3559, 15.0795]]).T),
    2: get_transformation_matrix(rotation_by_240d, np.array([[8.2042 - 0.8837, 1.3559, 16.1851]]).T),
    3: get_transformation_matrix(rotation_by_180d, np.array([[8.2042 - 4.9827, 1.4511, 16.5793]]).T),
    4: get_transformation_matrix(rotation_by_180d, np.array([[8.2042 - 5.5479, 1.4511, 16.5793]]).T),
    5: get_transformation_matrix(rotation_by_90d, np.array([[8.2042 - 8.2042, 1.3559, 14.7008]]).T),
    6: get_transformation_matrix(rotation_by_90d, np.array([[8.2042 - 8.2042, 1.3559, 1.8415]]).T),
    7: get_transformation_matrix(no_rotation, np.array([[8.2042 - 5.5479, 1.4511, -0.0381]]).T),# the negative is intentional - the tag is set back
    8: get_transformation_matrix(no_rotation, np.array([[8.2042 - 4.9827, 1.4511, -0.0381]]).T),# the negative is intentional - the tag is set back
    9: get_transformation_matrix(rotation_by_300d, np.array([[8.2042 - 0.8837, 1.3559, 0.3561]]).T),
    10: get_transformation_matrix(rotation_by_300d, np.array([[8.2042 - 0.2459, 1.3559, 1.4615]]).T),
    11: get_transformation_matrix(rotation_by_60d, np.array([[8.2042 - 3.7132, 1.3208, 11.9047]]).T),
    12: get_transformation_matrix(rotation_by_300d, np.array([[8.2042 - 4.4983, 1.3208, 11.9047]]).T),
    13: get_transformation_matrix(rotation_by_180d, np.array([[8.2042 - 4.1051, 1.3208, 11.2202]]).T),
    14: get_transformation_matrix(no_rotation, np.array([[8.2042 - 4.1051, 1.3208, 5.3208]]).T),
    15: get_transformation_matrix(rotation_by_240d, np.array([[8.2042 - 1.3208, 4.6413, 4.4983]]).T),
    16: get_transformation_matrix(rotation_by_120d, np.array([[8.2042 - 3.7132, 4.6413, 4.4983]]).T)
}



def estimate_pose(tag):
    '''
    Get's the global pose based on the detector's output.
    Input: tag object
    Output: global pose as a pose matrix. 
    See the comments on the dictionary above and the documentation doc for information about the coordinate system used.
    '''

    # Gets transformation matrix for global to apriltag
    global_to_tag = global_to_tag_transformations[tag.tag_id]

    # Gets tag to camera by inverting camera to tag
    camera_to_tag = get_transformation_matrix(np.matmul(rotation_by_180d, tag.pose_R), tag.pose_t)
    tag_to_camera = np.linalg.inv(camera_to_tag)

    #position of camera in robot frame
    robot_to_camera = np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])#TODO: PLACEHOLDER VALUES
    
    #position of robot in camera frame
    camera_to_robot = np.linalg.inv(robot_to_camera)

    # Combines to get global to camera
    global_to_camera = np.matmul(global_to_tag, tag_to_camera)

    # Combines to get global to robot
    global_to_robot = np.matmul(global_to_camera, camera_to_robot)

    # Returns
    return global_to_robot



def is_tag_valid(tag):
    '''
    Input: tag object
    Ouptut: if the tag's ID is between 1-16
    '''

    return tag.tag_id in global_to_tag_transformations.keys()

def get_xyz(global_to_camera):

    # Pygame DRAW
    X = global_to_camera[0,3]
    Y = global_to_camera[1,3]
    Z = global_to_camera[2,3]

    return (X, Y, Z)


def convert_for_export(global_pose):
    ''' 
    Turns the robot's pose into a representation equivalent to that used by the WPILib Pose Estimators.
    Input: transformation matrix 
    Output: a vector containing the x and y coordinates as well as the counterclockwise angle parallel to the plane of the field from the x-axis in RADIANS.
    '''
    r =  Rotation.from_matrix(global_pose[:3, :3])
    # angles are euler angles in RADIANS
    angles = r.as_euler("xyz")
    x = global_pose[2,3]
    y = 8.2042 - global_pose[0, 3]
    pose = np.array([x, y, 2 * math.pi - r[1]])
    return pose


#####################################
if __name__ == "__main__":

    #from pupil_apriltags 

    g_to_t = global_to_tag_transformations[1]
    
    t_to_r = np.linalg.inv(np.array([
                     [1,0,0,0],
                     [0,1,0,0],
                     [0,0,1,0],
                     [0,0,0,1]]))
    
    multiplied = np.matmul(g_to_t, t_to_r)


    #print(estimate_pose(tag=Tag))
    #print(g_to_t)
    print(multiplied)