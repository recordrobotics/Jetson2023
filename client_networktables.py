from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)

def initialize_networktables(ip):
    NetworkTables.initialize(server=ip)

def put_pose(pose):
    sd = NetworkTables.getTable("JetsonVision")
    #for i in range(0, len(pose)):
    sd.putNumberArray("Pose", pose)

def put_tag_id(id):
    sd = NetworkTables.getTable("JetsonVision")
    sd.putNumber("Tag ID", id)

def put_has_pose(hasPose):
    sd = NetworkTables.getTable("JetsonVision")
    sd.putBoolean("Has pose", hasPose)
