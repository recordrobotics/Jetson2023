from __future__ import annotations
import typing
import wpimath_download.units
from . import constraint
from . import controller
from . import estimator
from . import optimization
from . import path
from . import plant
from . import system
from . import trajectory
__all__ = ['DifferentialDriveFeedforward', 'constraint', 'controller', 'estimator', 'optimization', 'path', 'plant', 'system', 'trajectory']
class DifferentialDriveFeedforward:
    """
    A helper class which computes the feedforward outputs for a differential
    drive drivetrain.
    """
    @typing.overload
    def __init__(self, kVLinear: wpimath_download.units.volt_seconds_per_meter, kALinear: wpimath_download.units.volt_seconds_squared_per_meter, kVAngular: wpimath_download.units.volt_seconds_per_radian, kAAngular: wpimath_download.units.volt_seconds_squared_per_radian, trackwidth: wpimath_download.units.meters) -> None:
        """
        Creates a new DifferentialDriveFeedforward with the specified parameters.
        
        :param kVLinear:   The linear velocity gain in volts per (meters per second).
        :param kALinear:   The linear acceleration gain in volts per (meters per
                           second squared).
        :param kVAngular:  The angular velocity gain in volts per (radians per
                           second).
        :param kAAngular:  The angular acceleration gain in volts per (radians per
                           second squared).
        :param trackwidth: The distance between the differential drive's left and
                           right wheels, in meters.
        """
    @typing.overload
    def __init__(self, kVLinear: wpimath_download.units.volt_seconds_per_meter, kALinear: wpimath_download.units.volt_seconds_squared_per_meter, kVAngular: wpimath_download.units.volt_seconds_per_meter, kAAngular: wpimath_download.units.volt_seconds_squared_per_meter) -> None:
        """
        Creates a new DifferentialDriveFeedforward with the specified parameters.
        
        :param kVLinear:  The linear velocity gain in volts per (meters per second).
        :param kALinear:  The linear acceleration gain in volts per (meters per
                          second squared).
        :param kVAngular: The angular velocity gain in volts per (meters per
                          second).
        :param kAAngular: The angular acceleration gain in volts per (meters per
                          second squared).
        """
    def calculate(self, currentLeftVelocity: wpimath_download.units.meters_per_second, nextLeftVelocity: wpimath_download.units.meters_per_second, currentRightVelocity: wpimath_download.units.meters_per_second, nextRightVelocity: wpimath_download.units.meters_per_second, dt: wpimath_download.units.seconds) -> controller.DifferentialDriveWheelVoltages:
        """
        Calculates the differential drive feedforward inputs given velocity
        setpoints.
        
        :param currentLeftVelocity:  The current left velocity of the differential
                                     drive in meters/second.
        :param nextLeftVelocity:     The next left velocity of the differential drive in
                                     meters/second.
        :param currentRightVelocity: The current right velocity of the differential
                                     drive in meters/second.
        :param nextRightVelocity:    The next right velocity of the differential drive
                                     in meters/second.
        :param dt:                   Discretization timestep.
        """
