from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)

def initialize_networktables(ip):
    NetworkTables.initialize(server=ip)

def put_on_networktables(x,y):
    sd = NetworkTables.getTable("SmartDashboard")
    sd.putNumber("X", x)
    sd.putNumber("Y", y)

