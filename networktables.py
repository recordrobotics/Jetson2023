# Imports
from networktables import NetworkTables

# Must write code to set up networktables connection first

def put_on_networktables(x, y):
        '''
        Input: x, y value
        Output: none, but puts on networktables as action
        '''

        # Adds values to networktables
        NetworkTables.getTable("SmartDashboard").putNumber("X", x)
        NetworkTables.getTable("SmartDashboard").putNumber("Y", y)

        # Returns
        return