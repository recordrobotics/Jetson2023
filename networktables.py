from networktables import NetworkTables

def draw_tags(x, y):
        NetworkTables.getTable("SmartDashboard").putNumber("X", x)
        NetworkTables.getTable("SmartDashboard").putNumber("Y", y)