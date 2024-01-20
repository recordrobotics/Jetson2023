from quaternions import matrixToAxisAngle


def estimate_pose(tag):
    # Gets rotational matrix from tag
    r = tag.pose_R

    # Calculates axis angles
    axis_angles = matrixToAxisAngle(r)
    theta = axis_angles[0]

    angle = axis_angles[1][2]


    print(angle)




"""
def is_tag_valid(tag):
    '''
    Input: tag object
    Ouptut: if the tag is between 1-8
    '''

    return tag.tag_id in global_to_tag_transformations.keys()
"""


if __name__ == "__main__":
    import cv2 as cv
    import time

    from detect_tags import detect_tags, filter_tags

    # Opens opencv video capture object
    cap = cv.VideoCapture(1)

    from draw_tags import draw_tags
    #from networktables import NetworkTables

    while(True):
        start_time = time.time()

        # Gets frame
        ret, frame = cap.read()

        # display color
        cv.imshow('frame',frame)

        # Detects tags
        tags = detect_tags(frame)
        filtered_tags = filter_tags(tags)
    
        # draw apriltag locations
        debug_image = draw_tags(frame, filtered_tags, time.time() - start_time)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

        cv.imshow('AprilTag Detect Demo', debug_image)

        if len(filtered_tags) > 0:
            estimate_pose(filtered_tags[0])
        
        # send values to networktables
        #networktables(tags)
        