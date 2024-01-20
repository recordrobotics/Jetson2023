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


# Rotational matrix that does nothing
no_rotation = np.array([[0,-1,0],
                        [0,0,1],
                        [-1,0,0]])


# Rotational matrix that rotates over z axis by pi 
rotation_by_pi = np.array([[0,1,0],
                           [0,0,1],
                           [1,0,0]])


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

    # Gets tag to camera by inverting camera to tag
    camera_to_tag = get_transformation_matrix(tag.pose_R, tag.pose_t)
    tag_to_camera = np.linalg.inv(camera_to_tag)

    # Combines to get global to camera
    global_to_camera = np.dot(tag_to_camera, global_to_tag)

    # Returns
    return global_to_camera



def is_tag_valid(tag):
    '''
    Input: tag object
    Ouptut: if the tag is between 1-8
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

    global_to_1 = global_to_tag_transformations[1]
    print(np.linalg.inv(global_to_1))

    math.cos(math.radians())

    matrix_1 = np.array([[]])