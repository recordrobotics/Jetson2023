# Imports
import math
import numpy as np



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


def get_transformation_matrix_rotate_t(rotation_matrix, translation_matrix):
    '''
    Input: rotation & translation matrix
    Output: transformation matrix
    applies the rotation to the translation matrix
    '''

    #change translation to work after rotation
    translation_matrix = np.matmul(np.linalg.inv(rotation_matrix), translation_matrix)#                    EXPERIMENTAL ADDITION

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

# Rotation matrix that rotates around z axis by pi 
'''
rotation_by_pi_z = np.array([[-1,0,0],
                           [0,-1,0],
                           [0,0,1]])
'''

# Rotation matrix that rotates around y by 180 degrees
rotation_by_180d = np.array([[-1,0,0],
                            [0,1,0],
                            [0,0,-1]])

# Rotation matrix that rotates around y by 120 degrees
rotation_by_120d = np.array([[ -0.5,  0,  0.8660254],#TODO: do we need to invert this in the tranformation?
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

# Transformation matrix for flipping z
flip_z_transform = get_transformation_matrix(flip_z, np.array([[0, 0, 0]]).T)

# test tag is tag 1. data from last year
'''global_to_tag_transformations_2023 = {
    1: get_transformation_matrix(no_rotation, np.array([[1.071626, 0.462788, 15.513558]]).T),#values changed for test
    2: get_transformation_matrix(rotation_by_180d, np.array([[15.513558, 2.748026, 0.462788]]).T),
    3: get_transformation_matrix(rotation_by_180d, np.array([[15.513558, 4.424426, 0.462788]]).T),
    4: get_transformation_matrix(rotation_by_180d, np.array([[16.178784, 6.749796, 0.695452]]).T),
    5: get_transformation_matrix(no_rotation, np.array([[0.36195, 6.749796, 0.695452]]).T),
    6: get_transformation_matrix(no_rotation, np.array([[1.02743, 4.424426, 0.462788]]).T),
    7: get_transformation_matrix(no_rotation, np.array([[1.02743, 2.748026, 0.462788]]).T),
    8: get_transformation_matrix(no_rotation, np.array([[1.02743, 1.071626, 0.462788]]).T),
}'''


'''
All distances are in meters.
The algebra below looks questionable, but that is because some adjustments were necessary to take into account the strange tag frame
z is flipped because the z axis in the tag frame is INTO the tag
To place the origin in the top left, the x coordinate of tag 6 was taken as the x coordinate of the origin
'''
global_to_tag_transformations = {
    1: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_120d), np.array([[8.2042 - 0.2459, 1.3559, 15.0795]]).T),#TODO: the x value is returning negative; this doesn't make sense
    2: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_120d), np.array([[8.2042 - 0.8837, 1.3559, 16.1851]]).T),#TODO: does the x axis in the rotation still need to be flipped?
    3: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_180d), np.array([[8.2042 - 4.9827, 1.4511, 16.5793]]).T),
    4: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_180d), np.array([[8.2042 - 5.5479, 1.4511, 16.5793]]).T),
    5: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_270d), np.array([[8.2042 - 8.2042, 1.3559, 14.7008]]).T),
    6: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_270d), np.array([[8.2042 - 8.2042, 1.3559, 1.8415]]).T),
    7: get_transformation_matrix(np.matmul(rotation_by_180d, no_rotation), np.array([[8.2042 - 5.5479, 1.4511, -0.0381]]).T),# the negative is intentional - the tag is set back
    8: get_transformation_matrix(np.matmul(rotation_by_180d, no_rotation), np.array([[8.2042 - 4.9827, 1.4511, -0.0381]]).T),# the negative is intentional - the tag is set back
    9: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_60d), np.array([[8.2042 - 0.8837, 1.3559, 0.3561]]).T),
    10: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_60d), np.array([[8.2042 - 0.2459, 1.3559, 1.4615]]).T),
    11: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_60d), np.array([[8.2042 - 3.7132, 1.3208, 11.9047]]).T),
    12: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_300d), np.array([[8.2042 - 4.4983, 1.3208, 11.9047]]).T),
    13: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_180d), np.array([[8.2042 - 4.1051, 1.3208, 11.2202]]).T),
    14: get_transformation_matrix(np.matmul(rotation_by_180d, no_rotation), np.array([[8.2042 - 4.1051, 1.3208, 5.3208]]).T),
    15: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_120d), np.array([[8.2042 - 1.3208, 4.6413, 4.4983]]).T),
    16: get_transformation_matrix(np.matmul(rotation_by_180d, rotation_by_240d), np.array([[8.2042 - 3.7132, 4.6413, 4.4983]]).T)
}



def estimate_pose(tag):
    '''
    Input: tag object
    Output: global pose in (x, y, z)
    '''

    # Gets transformation matrix for global to apriltag
    global_to_tag = global_to_tag_transformations[tag.tag_id]
    #print("g to t" + global_to_tag)

    # Gets tag to camera by inverting camera to tag
    camera_to_tag = get_transformation_matrix(tag.pose_R, tag.pose_t)
    #print("c to t" + camera_to_tag)
    tag_to_camera = np.linalg.inv(camera_to_tag)
    #print("t to c" + tag_to_camera)

    #position of camera in robot frame
    robot_to_camera = np.array([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 1, 0],
                                [0, 0, 0, 1]])#TODO: PLACEHOLDER VALUES
    
    #position of robot in camera frame
    camera_to_robot = np.linalg.inv(robot_to_camera)

    # Combines to get global to camera
    global_to_camera = np.matmul(global_to_tag, tag_to_camera)
    #print("g to c" + global_to_camera)

    # Combines to get global to robot
    global_to_robot = np.matmul(global_to_camera, camera_to_robot)

    # Returns
    return global_to_robot



def is_tag_valid(tag):
    '''
    Input: tag object
    Ouptut: if the tag is between 1-16
    '''

    return tag.tag_id in global_to_tag_transformations.keys()

def get_xyz(global_to_camera):

    # Pygame DRAW
    X = global_to_camera[0,3]
    Y = global_to_camera[1,3]
    Z = global_to_camera[2,3]

    return (X, Y, Z)

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