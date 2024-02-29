from __future__ import annotations
import wpimath_download.geometry._geometry
import wpimath_download.units
__all__ = ['angleModulus', 'applyDeadband', 'inputModulus', 'objectToRobotPose']
def angleModulus(angle: wpimath_download.units.radians) -> wpimath_download.units.radians:
    ...
def applyDeadband(value: float, deadband: float, maxMagnitude: float = 1.0) -> float:
    """
    Returns 0.0 if the given value is within the specified range around zero. The
    remaining range between the deadband and the maximum magnitude is scaled from
    0.0 to the maximum magnitude.
    
    :param value:        Value to clip.
    :param deadband:     Range around zero.
    :param maxMagnitude: The maximum magnitude of the input (defaults to 1). Can
                         be infinite.
    
    :returns: The value after the deadband is applied.
    """
def inputModulus(input: float, minimumInput: float, maximumInput: float) -> float:
    """
    Returns modulus of input.
    
    :param input:        Input value to wrap.
    :param minimumInput: The minimum value expected from the input.
    :param maximumInput: The maximum value expected from the input.
    """
def objectToRobotPose(objectInField: wpimath_download.geometry._geometry.Pose3d, cameraToObject: wpimath_download.geometry._geometry.Transform3d, robotToCamera: wpimath_download.geometry._geometry.Transform3d) -> wpimath_download.geometry._geometry.Pose3d:
    ...
