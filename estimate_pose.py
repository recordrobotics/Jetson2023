# Imports
import math
import pose3d
import numpy as np



def get_transformation_matrix(rotation_matrix, translation_matrix):
    '''
    Input: rotation & translation matrix
    Output: transformation matrix
    '''

    # Creates a matrix that is a concatenated rotation next to translation
    n1 = np.concatenate((rotation_matrix, translation_matrix), axis=1)

    print(n1)

    # Adds horizonal array of 0's below the existing matrix
    horizontal_array = np.array([[0,0,0,1]])
    n2 = np.concatenate((n1, horizontal_array), axis=0)

    # Returns
    return n2



# Rotational matrix that does nothing
no_rotation = np.array([[1,0,0],
                        [0,1,0],
                        [0,0,1]])

# Rotational matrix that rotates over z axis by pi 
rotation_by_pi = np.array([[-1,0,0],
                           [0,-1,0],
                           [0,0,1]])

# Tag locations and rotations along field
'''
tag_locations = {
    1: {"t": [15.513558, 1.071626, 0.462788], "r": rotation_by_pi},
    2: {"t": [15.513558, 2.748026, 0.462788], "r": rotation_by_pi},
    3: {"t": [15.513558, 4.424426, 0.462788], "r": rotation_by_pi},
    4: {"t": [16.178784, 6.749796, 0.695452], "r": rotation_by_pi},
    5: {"t": [0.36195, 6.749796, 0.695452], "r": no_rotation},
    6: {"t": [1.02743, 4.424426, 0.462788], "r": no_rotation},
    7: {"t": [1.02743, 2.748026, 0.462788], "r": no_rotation},
    8: {"t": [1.02743, 1.071626, 0.462788], "r": no_rotation},
}
'''

# Don't ask. I'm not proud of it
global_to_tag_transformations = {
    1: get_transformation_matrix(rotation_by_pi, np.array([[15.513558, 1.071626, 0.462788]]).T),
    2: get_transformation_matrix(rotation_by_pi, np.array([[15.513558, 2.748026, 0.462788]]).T),
    3: get_transformation_matrix(rotation_by_pi, np.array([[15.513558, 4.424426, 0.462788]]).T),
    4: get_transformation_matrix(rotation_by_pi, np.array([[16.178784, 6.749796, 0.695452]]).T),
    5: get_transformation_matrix(no_rotation, np.array([[0.36195, 6.749796, 0.695452]]).T),
    6: get_transformation_matrix(no_rotation, np.array([[1.02743, 4.424426, 0.462788]]).T),
    7: get_transformation_matrix(no_rotation, np.array([[1.02743, 2.748026, 0.462788]]).T),
    8: get_transformation_matrix(no_rotation, np.array([[1.02743, 1.071626, 0.462788]]).T),
}

def estimate_pose(tag):
    '''
    Input: tag object
    Output: global pose in (x, y, z)
    '''

    # Gets transformation matrix for global to apriltag
    global_to_tag = global_to_tag_transformations[tag.tag_id]

    # Gets camera to tag transformation
    camera_to_tag = get_transformation_matrix(tag.pose_R, tag.pose_t)

    # Inverts to get tag to camera transformation
    tag_to_camera = np.linalg.inv(camera_to_tag)

    # Combines to get global to camera
    global_to_camera = np.matmul(tag_to_camera, global_to_tag)

    # Returns
    return global_to_camera



def is_tag_valid(tag):
    '''
    Input: tag object
    Ouptut: if the tag is between 1-8
    '''

    return tag.tag_id in global_to_tag_transformations.keys()