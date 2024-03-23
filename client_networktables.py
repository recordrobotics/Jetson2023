from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)

def initialize_networktables(ip):
    NetworkTables.initialize(server=ip)

def put_pose(pose, id, latency):
    sd = NetworkTables.getTable("JetsonVision")
    sd.putNumberArray("Pose", [*pose, id, latency])

def put_has_pose(hasPose):
    sd = NetworkTables.getTable("JetsonVision")
    #print(hasPose)
    sd.putBoolean("Has pose", hasPose)
