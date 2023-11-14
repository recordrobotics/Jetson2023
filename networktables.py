from networktables import NetworkTables
from pupil_apriltags import Detector

def draw_tags(
    tags
):
    for tag in tags:
        NetworkTables.getTable("SmartDashboard").putNumber("pose_t" + tag.tag_id, tag.pose_t)
        NetworkTables.getTable("SmartDashboard").putNumber("pose_R" + tag.tag_id, tag.pose_R)
        NetworkTables.getTable("SmartDashboard").putNumber("pose_err" + tag.tag_id, tag.pose_err)