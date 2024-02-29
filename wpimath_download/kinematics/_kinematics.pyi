from __future__ import annotations
import typing
import wpimath_download.geometry._geometry
import wpimath_download.units
__all__ = ['ChassisSpeeds', 'DifferentialDriveKinematics', 'DifferentialDriveKinematicsBase', 'DifferentialDriveOdometry', 'DifferentialDriveOdometryBase', 'DifferentialDriveWheelPositions', 'DifferentialDriveWheelSpeeds', 'MecanumDriveKinematics', 'MecanumDriveKinematicsBase', 'MecanumDriveOdometry', 'MecanumDriveOdometryBase', 'MecanumDriveWheelPositions', 'MecanumDriveWheelSpeeds', 'SwerveDrive2Kinematics', 'SwerveDrive2KinematicsBase', 'SwerveDrive2Odometry', 'SwerveDrive2OdometryBase', 'SwerveDrive2WheelPositions', 'SwerveDrive3Kinematics', 'SwerveDrive3KinematicsBase', 'SwerveDrive3Odometry', 'SwerveDrive3OdometryBase', 'SwerveDrive3WheelPositions', 'SwerveDrive4Kinematics', 'SwerveDrive4KinematicsBase', 'SwerveDrive4Odometry', 'SwerveDrive4OdometryBase', 'SwerveDrive4WheelPositions', 'SwerveDrive6Kinematics', 'SwerveDrive6KinematicsBase', 'SwerveDrive6Odometry', 'SwerveDrive6OdometryBase', 'SwerveDrive6WheelPositions', 'SwerveModulePosition', 'SwerveModuleState']
class ChassisSpeeds:
    """
    Represents the speed of a robot chassis. Although this struct contains
    similar members compared to a Twist2d, they do NOT represent the same thing.
    Whereas a Twist2d represents a change in pose w.r.t to the robot frame of
    reference, a ChassisSpeeds struct represents a robot's velocity.
    
    A strictly non-holonomic drivetrain, such as a differential drive, should
    never have a dy component because it can never move sideways. Holonomic
    drivetrains such as swerve and mecanum will often have all three components.
    """
    WPIStruct: typing.ClassVar[typing.Any]  # value = <capsule object "WPyStruct" at 0x000002A5EF6C8A20>
    omega_dps: wpimath_download.units.degrees_per_second
    vx_fps: wpimath_download.units.feet_per_second
    vy_fps: wpimath_download.units.feet_per_second
    @staticmethod
    @typing.overload
    def discretize(vx: wpimath_download.units.meters_per_second, vy: wpimath_download.units.meters_per_second, omega: wpimath_download.units.radians_per_second, dt: wpimath_download.units.seconds) -> ChassisSpeeds:
        """
        Disretizes a continuous-time chassis speed.
        
        This function converts a continuous-time chassis speed into a discrete-time
        one such that when the discrete-time chassis speed is applied for one
        timestep, the robot moves as if the velocity components are independent
        (i.e., the robot moves v_x * dt along the x-axis, v_y * dt along the
        y-axis, and omega * dt around the z-axis).
        
        This is useful for compensating for translational skew when translating and
        rotating a swerve drivetrain.
        
        :param vx:    Forward velocity.
        :param vy:    Sideways velocity.
        :param omega: Angular velocity.
        :param dt:    The duration of the timestep the speeds should be applied for.
        
        :returns: Discretized ChassisSpeeds.
        """
    @staticmethod
    @typing.overload
    def discretize(continuousSpeeds: ChassisSpeeds, dt: wpimath_download.units.seconds) -> ChassisSpeeds:
        """
        Disretizes a continuous-time chassis speed.
        
        This function converts a continuous-time chassis speed into a discrete-time
        one such that when the discrete-time chassis speed is applied for one
        timestep, the robot moves as if the velocity components are independent
        (i.e., the robot moves v_x * dt along the x-axis, v_y * dt along the
        y-axis, and omega * dt around the z-axis).
        
        This is useful for compensating for translational skew when translating and
        rotating a swerve drivetrain.
        
        :param continuousSpeeds: The continuous speeds.
        :param dt:               The duration of the timestep the speeds should be applied for.
        
        :returns: Discretized ChassisSpeeds.
        """
    @staticmethod
    def fromFeet(vx: wpimath_download.units.feet_per_second = 0, vy: wpimath_download.units.feet_per_second = 0, omega: wpimath_download.units.radians_per_second = 0) -> ChassisSpeeds:
        ...
    @staticmethod
    @typing.overload
    def fromFieldRelativeSpeeds(vx: wpimath_download.units.meters_per_second, vy: wpimath_download.units.meters_per_second, omega: wpimath_download.units.radians_per_second, robotAngle: wpimath_download.geometry._geometry.Rotation2d) -> ChassisSpeeds:
        """
        Converts a user provided field-relative set of speeds into a robot-relative
        ChassisSpeeds object.
        
        :param vx:         The component of speed in the x direction relative to the field.
                           Positive x is away from your alliance wall.
        :param vy:         The component of speed in the y direction relative to the field.
                           Positive y is to your left when standing behind the alliance wall.
        :param omega:      The angular rate of the robot.
        :param robotAngle: The angle of the robot as measured by a gyroscope. The
                           robot's angle is considered to be zero when it is facing directly away from
                           your alliance station wall. Remember that this should be CCW positive.
        
        :returns: ChassisSpeeds object representing the speeds in the robot's frame
                  of reference.
        """
    @staticmethod
    @typing.overload
    def fromFieldRelativeSpeeds(fieldRelativeSpeeds: ChassisSpeeds, robotAngle: wpimath_download.geometry._geometry.Rotation2d) -> ChassisSpeeds:
        """
        Converts a user provided field-relative ChassisSpeeds object into a
        robot-relative ChassisSpeeds object.
        
        :param fieldRelativeSpeeds: The ChassisSpeeds object representing the speeds
                                    in the field frame of reference. Positive x is away from your alliance
                                    wall. Positive y is to your left when standing behind the alliance wall.
        :param robotAngle:          The angle of the robot as measured by a gyroscope. The
                                    robot's angle is considered to be zero when it is facing directly away
                                    from your alliance station wall. Remember that this should be CCW
                                    positive.
        
        :returns: ChassisSpeeds object representing the speeds in the robot's frame
                  of reference.
        """
    @staticmethod
    @typing.overload
    def fromRobotRelativeSpeeds(vx: wpimath_download.units.meters_per_second, vy: wpimath_download.units.meters_per_second, omega: wpimath_download.units.radians_per_second, robotAngle: wpimath_download.geometry._geometry.Rotation2d) -> ChassisSpeeds:
        """
        Converts a user provided robot-relative set of speeds into a field-relative
        ChassisSpeeds object.
        
        :param vx:         The component of speed in the x direction relative to the robot.
                           Positive x is towards the robot's front.
        :param vy:         The component of speed in the y direction relative to the robot.
                           Positive y is towards the robot's left.
        :param omega:      The angular rate of the robot.
        :param robotAngle: The angle of the robot as measured by a gyroscope. The
                           robot's angle is considered to be zero when it is facing directly away from
                           your alliance station wall. Remember that this should be CCW positive.
        
        :returns: ChassisSpeeds object representing the speeds in the field's frame
                  of reference.
        """
    @staticmethod
    @typing.overload
    def fromRobotRelativeSpeeds(robotRelativeSpeeds: ChassisSpeeds, robotAngle: wpimath_download.geometry._geometry.Rotation2d) -> ChassisSpeeds:
        """
        Converts a user provided robot-relative ChassisSpeeds object into a
        field-relative ChassisSpeeds object.
        
        :param robotRelativeSpeeds: The ChassisSpeeds object representing the speeds
                                    in the robot frame of reference. Positive x is the towards robot's
                                    front. Positive y is towards the robot's left.
        :param robotAngle:          The angle of the robot as measured by a gyroscope. The
                                    robot's angle is considered to be zero when it is facing directly away
                                    from your alliance station wall. Remember that this should be CCW
                                    positive.
        
        :returns: ChassisSpeeds object representing the speeds in the field's frame
                  of reference.
        """
    def __add__(self, arg0: ChassisSpeeds) -> ChassisSpeeds:
        """
        Adds two ChassisSpeeds and returns the sum.
        
        For example, ChassisSpeeds{1.0, 0.5, 1.5} + ChassisSpeeds{2.0, 1.5, 0.5}
        = ChassisSpeeds{3.0, 2.0, 2.0}
        
        :param other: The ChassisSpeeds to add.
        
        :returns: The sum of the ChassisSpeeds.
        """
    def __getitem__(self, arg0: int) -> float:
        ...
    def __init__(self, vx: wpimath_download.units.meters_per_second = 0, vy: wpimath_download.units.meters_per_second = 0, omega: wpimath_download.units.radians_per_second = 0) -> None:
        ...
    def __len__(self) -> int:
        ...
    def __mul__(self, arg0: float) -> ChassisSpeeds:
        """
        Multiplies the ChassisSpeeds by a scalar and returns the new ChassisSpeeds.
        
        For example, ChassisSpeeds{2.0, 2.5, 1.0} * 2
        = ChassisSpeeds{4.0, 5.0, 1.0}
        
        :param scalar: The scalar to multiply by.
        
        :returns: The scaled ChassisSpeeds.
        """
    def __neg__(self) -> ChassisSpeeds:
        """
        Returns the inverse of the current ChassisSpeeds.
        This is equivalent to negating all components of the ChassisSpeeds.
        
        :returns: The inverse of the current ChassisSpeeds.
        """
    def __repr__(self) -> str:
        ...
    def __sub__(self, arg0: ChassisSpeeds) -> ChassisSpeeds:
        """
        Subtracts the other ChassisSpeeds from the current ChassisSpeeds and
        returns the difference.
        
        For example, ChassisSpeeds{5.0, 4.0, 2.0} - ChassisSpeeds{1.0, 2.0, 1.0}
        = ChassisSpeeds{4.0, 2.0, 1.0}
        
        :param other: The ChassisSpeeds to subtract.
        
        :returns: The difference between the two ChassisSpeeds.
        """
    def __truediv__(self, arg0: float) -> ChassisSpeeds:
        """
        Divides the ChassisSpeeds by a scalar and returns the new ChassisSpeeds.
        
        For example, ChassisSpeeds{2.0, 2.5, 1.0} / 2
        = ChassisSpeeds{1.0, 1.25, 0.5}
        
        :param scalar: The scalar to divide by.
        
        :returns: The scaled ChassisSpeeds.
        """
    @property
    def omega(self) -> wpimath_download.units.radians_per_second:
        """
        Represents the angular velocity of the robot frame. (CCW is +)
        """
    @omega.setter
    def omega(self, arg0: wpimath_download.units.radians_per_second) -> None:
        ...
    @property
    def vx(self) -> wpimath_download.units.meters_per_second:
        """
        Velocity along the x-axis. (Fwd is +)
        """
    @vx.setter
    def vx(self, arg0: wpimath_download.units.meters_per_second) -> None:
        ...
    @property
    def vy(self) -> wpimath_download.units.meters_per_second:
        """
        Velocity along the y-axis. (Left is +)
        """
    @vy.setter
    def vy(self, arg0: wpimath_download.units.meters_per_second) -> None:
        ...
class DifferentialDriveKinematics(DifferentialDriveKinematicsBase):
    """
    Helper class that converts a chassis velocity (dx and dtheta components) to
    left and right wheel velocities for a differential drive.
    
    Inverse kinematics converts a desired chassis speed into left and right
    velocity components whereas forward kinematics converts left and right
    component velocities into a linear and angular chassis speed.
    """
    WPIStruct: typing.ClassVar[typing.Any]  # value = <capsule object "WPyStruct" at 0x000002A5EF69F150>
    def __init__(self, trackWidth: wpimath_download.units.meters) -> None:
        """
        Constructs a differential drive kinematics object.
        
        :param trackWidth: The track width of the drivetrain. Theoretically, this is
                           the distance between the left wheels and right wheels. However, the
                           empirical value may be larger than the physical measured value due to
                           scrubbing effects.
        """
    def toChassisSpeeds(self, wheelSpeeds: DifferentialDriveWheelSpeeds) -> ChassisSpeeds:
        """
        Returns a chassis speed from left and right component velocities using
        forward kinematics.
        
        :param wheelSpeeds: The left and right velocities.
        
        :returns: The chassis speed.
        """
    @typing.overload
    def toTwist2d(self, leftDistance: wpimath_download.units.meters, rightDistance: wpimath_download.units.meters) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Returns a twist from left and right distance deltas using
        forward kinematics.
        
        :param leftDistance:  The distance measured by the left encoder.
        :param rightDistance: The distance measured by the right encoder.
        
        :returns: The resulting Twist2d.
        """
    @typing.overload
    def toTwist2d(self, start: DifferentialDriveWheelPositions, end: DifferentialDriveWheelPositions) -> wpimath_download.geometry._geometry.Twist2d:
        ...
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> DifferentialDriveWheelSpeeds:
        """
        Returns left and right component velocities from a chassis speed using
        inverse kinematics.
        
        :param chassisSpeeds: The linear and angular (dx and dtheta) components that
                              represent the chassis' speed.
        
        :returns: The left and right velocities.
        """
    @property
    def trackWidth(self) -> wpimath_download.units.meters:
        """
        Differential drive trackwidth.
        """
class DifferentialDriveKinematicsBase:
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual wheel speeds. Robot code should not use this directly-
    Instead, use the particular type for your drivetrain (e.g.,
    DifferentialDriveKinematics).
    
    Inverse kinematics converts a desired chassis speed into wheel speeds whereas
    forward kinematics converts wheel speeds into chassis speed.
    """
    def __init__(self) -> None:
        ...
    def toChassisSpeeds(self, wheelSpeeds: DifferentialDriveWheelSpeeds) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis speed from the
        wheel speeds. This method is often used for odometry -- determining the
        robot's position on the field using data from the real-world speed of each
        wheel on the robot.
        
        :param wheelSpeeds: The speeds of the wheels.
        
        :returns: The chassis speed.
        """
    def toTwist2d(self, start: DifferentialDriveWheelPositions, end: DifferentialDriveWheelPositions) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the given
        change in wheel positions. This method is often used for odometry --
        determining the robot's position on the field using changes in the distance
        driven by each wheel on the robot.
        
        :param start: The starting distances driven by the wheels.
        :param end:   The ending distances driven by the wheels.
        
        :returns: The resulting Twist2d in the robot's movement.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> DifferentialDriveWheelSpeeds:
        """
        Performs inverse kinematics to return the wheel speeds from a desired
        chassis velocity. This method is often used to convert joystick values into
        wheel speeds.
        
        :param chassisSpeeds: The desired chassis speed.
        
        :returns: The wheel speeds.
        """
class DifferentialDriveOdometry(DifferentialDriveOdometryBase):
    """
    Class for differential drive odometry. Odometry allows you to track the
    robot's position on the field over the course of a match using readings from
    2 encoders and a gyroscope.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    
    It is important that you reset your encoders to zero before using this class.
    Any subsequent pose resets also require the encoders to be reset to zero.
    """
    def __init__(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, leftDistance: wpimath_download.units.meters, rightDistance: wpimath_download.units.meters, initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs a DifferentialDriveOdometry object.
        
        IF leftDistance and rightDistance are unspecified,
        You NEED to reset your encoders (to zero).
        
        :param gyroAngle:     The angle reported by the gyroscope.
        :param leftDistance:  The distance traveled by the left encoder.
        :param rightDistance: The distance traveled by the right encoder.
        :param initialPose:   The starting position of the robot on the field.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, leftDistance: wpimath_download.units.meters, rightDistance: wpimath_download.units.meters, pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        IF leftDistance and rightDistance are unspecified,
        You NEED to reset your encoders (to zero).
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param pose:          The position on the field that your robot is at.
        :param gyroAngle:     The angle reported by the gyroscope.
        :param leftDistance:  The distance traveled by the left encoder.
        :param rightDistance: The distance traveled by the right encoder.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, leftDistance: wpimath_download.units.meters, rightDistance: wpimath_download.units.meters) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot position on the field using distance measurements from
        encoders. This method is more numerically accurate than using velocities to
        integrate the pose and is also advantageous for teams that are using lower
        CPR encoders.
        
        :param gyroAngle:     The angle reported by the gyroscope.
        :param leftDistance:  The distance traveled by the left encoder.
        :param rightDistance: The distance traveled by the right encoder.
        
        :returns: The new pose of the robot.
        """
class DifferentialDriveOdometryBase:
    """
    Class for odometry. Robot code should not use this directly- Instead, use the
    particular type for your drivetrain (e.g., DifferentialDriveOdometry).
    Odometry allows you to track the robot's position on the field over a course
    of a match using readings from your wheel encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    
    @tparam WheelSpeeds Wheel speeds type.
    @tparam WheelPositions Wheel positions type.
    """
    def __init__(self, kinematics: DifferentialDriveKinematicsBase, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: DifferentialDriveWheelPositions, initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs an Odometry object.
        
        :param kinematics:     The kinematics for your drivetrain.
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param initialPose:    The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Returns the position of the robot on the field.
        
        :returns: The pose of the robot.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: DifferentialDriveWheelPositions, pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param pose:           The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: DifferentialDriveWheelPositions) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics, in addition to the current distance measurement at each wheel.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        
        :returns: The new pose of the robot.
        """
class DifferentialDriveWheelPositions:
    """
    Represents the wheel positions for a differential drive drivetrain.
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: DifferentialDriveWheelPositions) -> bool:
        """
        Checks equality between this DifferentialDriveWheelPositions and another
        object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are equal.
        """
    def __init__(self) -> None:
        ...
    def __ne__(self, arg0: DifferentialDriveWheelPositions) -> bool:
        """
        Checks inequality between this DifferentialDriveWheelPositions and another
        object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are not equal.
        """
    def interpolate(self, endValue: DifferentialDriveWheelPositions, t: float) -> DifferentialDriveWheelPositions:
        ...
    @property
    def left(self) -> wpimath_download.units.meters:
        """
        Distance driven by the left side.
        """
    @left.setter
    def left(self, arg0: wpimath_download.units.meters) -> None:
        ...
    @property
    def right(self) -> wpimath_download.units.meters:
        """
        Distance driven by the right side.
        """
    @right.setter
    def right(self, arg0: wpimath_download.units.meters) -> None:
        ...
class DifferentialDriveWheelSpeeds:
    """
    Represents the wheel speeds for a differential drive drivetrain.
    """
    WPIStruct: typing.ClassVar[typing.Any]  # value = <capsule object "WPyStruct" at 0x000002A5EF6C8FF0>
    left_fps: wpimath_download.units.feet_per_second
    right_fps: wpimath_download.units.feet_per_second
    @staticmethod
    def fromFeet(left: wpimath_download.units.feet_per_second, right: wpimath_download.units.feet_per_second) -> DifferentialDriveWheelSpeeds:
        ...
    def __add__(self, arg0: DifferentialDriveWheelSpeeds) -> DifferentialDriveWheelSpeeds:
        """
        Adds two DifferentialDriveWheelSpeeds and returns the sum.
        
        For example, DifferentialDriveWheelSpeeds{1.0, 0.5} +
        DifferentialDriveWheelSpeeds{2.0, 1.5} =
        DifferentialDriveWheelSpeeds{3.0, 2.0}
        
        :param other: The DifferentialDriveWheelSpeeds to add.
        
        :returns: The sum of the DifferentialDriveWheelSpeeds.
        """
    def __init__(self, left: wpimath_download.units.meters_per_second = 0, right: wpimath_download.units.meters_per_second = 0) -> None:
        ...
    def __mul__(self, arg0: float) -> DifferentialDriveWheelSpeeds:
        """
        Multiplies the DifferentialDriveWheelSpeeds by a scalar and returns the new
        DifferentialDriveWheelSpeeds.
        
        For example, DifferentialDriveWheelSpeeds{2.0, 2.5} * 2
        = DifferentialDriveWheelSpeeds{4.0, 5.0}
        
        :param scalar: The scalar to multiply by.
        
        :returns: The scaled DifferentialDriveWheelSpeeds.
        """
    def __neg__(self) -> DifferentialDriveWheelSpeeds:
        """
        Returns the inverse of the current DifferentialDriveWheelSpeeds.
        This is equivalent to negating all components of the
        DifferentialDriveWheelSpeeds.
        
        :returns: The inverse of the current DifferentialDriveWheelSpeeds.
        """
    def __repr__(self) -> str:
        ...
    def __sub__(self, arg0: DifferentialDriveWheelSpeeds) -> DifferentialDriveWheelSpeeds:
        """
        Subtracts the other DifferentialDriveWheelSpeeds from the current
        DifferentialDriveWheelSpeeds and returns the difference.
        
        For example, DifferentialDriveWheelSpeeds{5.0, 4.0} -
        DifferentialDriveWheelSpeeds{1.0, 2.0} =
        DifferentialDriveWheelSpeeds{4.0, 2.0}
        
        :param other: The DifferentialDriveWheelSpeeds to subtract.
        
        :returns: The difference between the two DifferentialDriveWheelSpeeds.
        """
    def __truediv__(self, arg0: float) -> DifferentialDriveWheelSpeeds:
        """
        Divides the DifferentialDriveWheelSpeeds by a scalar and returns the new
        DifferentialDriveWheelSpeeds.
        
        For example, DifferentialDriveWheelSpeeds{2.0, 2.5} / 2
        = DifferentialDriveWheelSpeeds{1.0, 1.25}
        
        :param scalar: The scalar to divide by.
        
        :returns: The scaled DifferentialDriveWheelSpeeds.
        """
    def desaturate(self, attainableMaxSpeed: wpimath_download.units.meters_per_second) -> None:
        """
        Renormalizes the wheel speeds if either side is above the specified
        maximum.
        
        Sometimes, after inverse kinematics, the requested speed from one or more
        wheels may be above the max attainable speed for the driving motor on that
        wheel. To fix this issue, one can reduce all the wheel speeds to make sure
        that all requested module speeds are at-or-below the absolute threshold,
        while maintaining the ratio of speeds between wheels.
        
        :param attainableMaxSpeed: The absolute max speed that a wheel can reach.
        """
    @property
    def left(self) -> wpimath_download.units.meters_per_second:
        """
        Speed of the left side of the robot.
        """
    @left.setter
    def left(self, arg0: wpimath_download.units.meters_per_second) -> None:
        ...
    @property
    def right(self) -> wpimath_download.units.meters_per_second:
        """
        Speed of the right side of the robot.
        """
    @right.setter
    def right(self, arg0: wpimath_download.units.meters_per_second) -> None:
        ...
class MecanumDriveKinematics(MecanumDriveKinematicsBase):
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual wheel speeds.
    
    The inverse kinematics (converting from a desired chassis velocity to
    individual wheel speeds) uses the relative locations of the wheels with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.
    
    Forward kinematics (converting an array of wheel speeds into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.
    
    The inverse kinematics: [wheelSpeeds] = [wheelLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [wheelLocations] and then
    multiply by [wheelSpeeds] to get our chassis speeds.
    
    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    WPIStruct: typing.ClassVar[typing.Any]  # value = <capsule object "WPyStruct" at 0x000002A5EF69ECA0>
    def __init__(self, frontLeftWheel: wpimath_download.geometry._geometry.Translation2d, frontRightWheel: wpimath_download.geometry._geometry.Translation2d, rearLeftWheel: wpimath_download.geometry._geometry.Translation2d, rearRightWheel: wpimath_download.geometry._geometry.Translation2d) -> None:
        """
        Constructs a mecanum drive kinematics object.
        
        :param frontLeftWheel:  The location of the front-left wheel relative to the
                                physical center of the robot.
        :param frontRightWheel: The location of the front-right wheel relative to
                                the physical center of the robot.
        :param rearLeftWheel:   The location of the rear-left wheel relative to the
                                physical center of the robot.
        :param rearRightWheel:  The location of the rear-right wheel relative to the
                                physical center of the robot.
        """
    def getFrontLeft(self) -> wpimath_download.geometry._geometry.Translation2d:
        """
        Returns the front-left wheel translation.
        
        :returns: The front-left wheel translation.
        """
    def getFrontRight(self) -> wpimath_download.geometry._geometry.Translation2d:
        """
        Returns the front-right wheel translation.
        
        :returns: The front-right wheel translation.
        """
    def getRearLeft(self) -> wpimath_download.geometry._geometry.Translation2d:
        """
        Returns the rear-left wheel translation.
        
        :returns: The rear-left wheel translation.
        """
    def getRearRight(self) -> wpimath_download.geometry._geometry.Translation2d:
        """
        Returns the rear-right wheel translation.
        
        :returns: The rear-right wheel translation.
        """
    def toChassisSpeeds(self, wheelSpeeds: MecanumDriveWheelSpeeds) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis state from the
        given wheel speeds. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed of
        each wheel on the robot.
        
        :param wheelSpeeds: The current mecanum drive wheel speeds.
        
        :returns: The resulting chassis speed.
        """
    @typing.overload
    def toTwist2d(self, start: MecanumDriveWheelPositions, end: MecanumDriveWheelPositions) -> wpimath_download.geometry._geometry.Twist2d:
        ...
    @typing.overload
    def toTwist2d(self, wheelDeltas: MecanumDriveWheelPositions) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the
        given wheel position deltas. This method is often used for odometry --
        determining the robot's position on the field using data from the
        distance driven by each wheel on the robot.
        
        :param wheelDeltas: The change in distance driven by each wheel.
        
        :returns: The resulting chassis speed.
        """
    @typing.overload
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath_download.geometry._geometry.Translation2d) -> MecanumDriveWheelSpeeds:
        """
        Performs inverse kinematics to return the wheel speeds from a desired
        chassis velocity. This method is often used to convert joystick values into
        wheel speeds.
        
        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.
        
        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
                                 center of rotation at one corner of the robot and
                                 provide a chassis speed that only has a dtheta
                                 component, the robot will rotate around that
                                 corner.
        
        :returns: The wheel speeds. Use caution because they are not normalized.
                  Sometimes, a user input may cause one of the wheel speeds to go
                  above the attainable max velocity. Use the
                  :meth:`MecanumDriveWheelSpeeds.normalize` method to rectify
                  this issue. In addition, you can use Python unpacking syntax
                  to directly assign the wheel speeds to variables::
        
                    fl, fr, bl, br = kinematics.toWheelSpeeds(chassisSpeeds)
        """
    @typing.overload
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> MecanumDriveWheelSpeeds:
        """
        Performs inverse kinematics to return the wheel speeds from a desired
        chassis velocity. This method is often used to convert joystick values into
        wheel speeds.
        
        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.
        
        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
                                 center of rotation at one corner of the robot and
                                 provide a chassis speed that only has a dtheta
                                 component, the robot will rotate around that
                                 corner.
        
        :returns: The wheel speeds. Use caution because they are not normalized.
                  Sometimes, a user input may cause one of the wheel speeds to go
                  above the attainable max velocity. Use the
                  :meth:`MecanumDriveWheelSpeeds.normalize` method to rectify
                  this issue. In addition, you can use Python unpacking syntax
                  to directly assign the wheel speeds to variables::
        
                    fl, fr, bl, br = kinematics.toWheelSpeeds(chassisSpeeds)
        """
class MecanumDriveKinematicsBase:
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual wheel speeds. Robot code should not use this directly-
    Instead, use the particular type for your drivetrain (e.g.,
    DifferentialDriveKinematics).
    
    Inverse kinematics converts a desired chassis speed into wheel speeds whereas
    forward kinematics converts wheel speeds into chassis speed.
    """
    def __init__(self) -> None:
        ...
    def toChassisSpeeds(self, wheelSpeeds: MecanumDriveWheelSpeeds) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis speed from the
        wheel speeds. This method is often used for odometry -- determining the
        robot's position on the field using data from the real-world speed of each
        wheel on the robot.
        
        :param wheelSpeeds: The speeds of the wheels.
        
        :returns: The chassis speed.
        """
    def toTwist2d(self, start: MecanumDriveWheelPositions, end: MecanumDriveWheelPositions) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the given
        change in wheel positions. This method is often used for odometry --
        determining the robot's position on the field using changes in the distance
        driven by each wheel on the robot.
        
        :param start: The starting distances driven by the wheels.
        :param end:   The ending distances driven by the wheels.
        
        :returns: The resulting Twist2d in the robot's movement.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> MecanumDriveWheelSpeeds:
        """
        Performs inverse kinematics to return the wheel speeds from a desired
        chassis velocity. This method is often used to convert joystick values into
        wheel speeds.
        
        :param chassisSpeeds: The desired chassis speed.
        
        :returns: The wheel speeds.
        """
class MecanumDriveOdometry(MecanumDriveOdometryBase):
    """
    Class for mecanum drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    mecanum wheel encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: MecanumDriveKinematics, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: MecanumDriveWheelPositions, initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs a MecanumDriveOdometry object.
        
        :param kinematics:     The mecanum drive kinematics for your drivetrain.
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param initialPose:    The starting position of the robot on the field.
        """
class MecanumDriveOdometryBase:
    """
    Class for odometry. Robot code should not use this directly- Instead, use the
    particular type for your drivetrain (e.g., DifferentialDriveOdometry).
    Odometry allows you to track the robot's position on the field over a course
    of a match using readings from your wheel encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    
    @tparam WheelSpeeds Wheel speeds type.
    @tparam WheelPositions Wheel positions type.
    """
    def __init__(self, kinematics: MecanumDriveKinematicsBase, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: MecanumDriveWheelPositions, initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs an Odometry object.
        
        :param kinematics:     The kinematics for your drivetrain.
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param initialPose:    The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Returns the position of the robot on the field.
        
        :returns: The pose of the robot.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: MecanumDriveWheelPositions, pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param pose:           The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: MecanumDriveWheelPositions) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics, in addition to the current distance measurement at each wheel.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        
        :returns: The new pose of the robot.
        """
class MecanumDriveWheelPositions:
    """
    Represents the wheel positions for a mecanum drive drivetrain.
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: MecanumDriveWheelPositions) -> bool:
        """
        Checks equality between this MecanumDriveWheelPositions and another object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are equal.
        """
    def __init__(self) -> None:
        ...
    def __ne__(self, arg0: MecanumDriveWheelPositions) -> bool:
        """
        Checks inequality between this MecanumDriveWheelPositions and another
        object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are not equal.
        """
    def interpolate(self, endValue: MecanumDriveWheelPositions, t: float) -> MecanumDriveWheelPositions:
        ...
    @property
    def frontLeft(self) -> wpimath_download.units.meters:
        """
        Distance driven by the front-left wheel.
        """
    @frontLeft.setter
    def frontLeft(self, arg0: wpimath_download.units.meters) -> None:
        ...
    @property
    def frontRight(self) -> wpimath_download.units.meters:
        """
        Distance driven by the front-right wheel.
        """
    @frontRight.setter
    def frontRight(self, arg0: wpimath_download.units.meters) -> None:
        ...
    @property
    def rearLeft(self) -> wpimath_download.units.meters:
        """
        Distance driven by the rear-left wheel.
        """
    @rearLeft.setter
    def rearLeft(self, arg0: wpimath_download.units.meters) -> None:
        ...
    @property
    def rearRight(self) -> wpimath_download.units.meters:
        """
        Distance driven by the rear-right wheel.
        """
    @rearRight.setter
    def rearRight(self, arg0: wpimath_download.units.meters) -> None:
        ...
class MecanumDriveWheelSpeeds:
    """
    Represents the wheel speeds for a mecanum drive drivetrain.
    """
    WPIStruct: typing.ClassVar[typing.Any]  # value = <capsule object "WPyStruct" at 0x000002A5EF6CB600>
    frontLeft_fps: wpimath_download.units.feet_per_second
    frontRight_fps: wpimath_download.units.feet_per_second
    rearLeft_fps: wpimath_download.units.feet_per_second
    rearRight_fps: wpimath_download.units.feet_per_second
    @staticmethod
    def fromFeet(frontLeft: wpimath_download.units.feet_per_second, frontRight: wpimath_download.units.feet_per_second, rearLeft: wpimath_download.units.feet_per_second, rearRight: wpimath_download.units.feet_per_second) -> MecanumDriveWheelSpeeds:
        ...
    def __add__(self, arg0: MecanumDriveWheelSpeeds) -> MecanumDriveWheelSpeeds:
        """
        Adds two MecanumDriveWheelSpeeds and returns the sum.
        
        For example, MecanumDriveWheelSpeeds{1.0, 0.5, 2.0, 1.5} +
        MecanumDriveWheelSpeeds{2.0, 1.5, 0.5, 1.0} =
        MecanumDriveWheelSpeeds{3.0, 2.0, 2.5, 2.5}
        
        :param other: The MecanumDriveWheelSpeeds to add.
        
        :returns: The sum of the MecanumDriveWheelSpeeds.
        """
    def __init__(self, frontLeft: wpimath_download.units.meters_per_second = 0, frontRight: wpimath_download.units.meters_per_second = 0, rearLeft: wpimath_download.units.meters_per_second = 0, rearRight: wpimath_download.units.meters_per_second = 0) -> None:
        ...
    def __mul__(self, arg0: float) -> MecanumDriveWheelSpeeds:
        """
        Multiplies the MecanumDriveWheelSpeeds by a scalar and returns the new
        MecanumDriveWheelSpeeds.
        
        For example, MecanumDriveWheelSpeeds{2.0, 2.5, 3.0, 3.5} * 2 =
        MecanumDriveWheelSpeeds{4.0, 5.0, 6.0, 7.0}
        
        :param scalar: The scalar to multiply by.
        
        :returns: The scaled MecanumDriveWheelSpeeds.
        """
    def __neg__(self) -> MecanumDriveWheelSpeeds:
        """
        Returns the inverse of the current MecanumDriveWheelSpeeds.
        This is equivalent to negating all components of the
        MecanumDriveWheelSpeeds.
        
        :returns: The inverse of the current MecanumDriveWheelSpeeds.
        """
    def __repr__(self) -> str:
        ...
    def __sub__(self, arg0: MecanumDriveWheelSpeeds) -> MecanumDriveWheelSpeeds:
        """
        Subtracts the other MecanumDriveWheelSpeeds from the current
        MecanumDriveWheelSpeeds and returns the difference.
        
        For example, MecanumDriveWheelSpeeds{5.0, 4.0, 6.0, 2.5} -
        MecanumDriveWheelSpeeds{1.0, 2.0, 3.0, 0.5} =
        MecanumDriveWheelSpeeds{4.0, 2.0, 3.0, 2.0}
        
        :param other: The MecanumDriveWheelSpeeds to subtract.
        
        :returns: The difference between the two MecanumDriveWheelSpeeds.
        """
    def __truediv__(self, arg0: float) -> MecanumDriveWheelSpeeds:
        """
        Divides the MecanumDriveWheelSpeeds by a scalar and returns the new
        MecanumDriveWheelSpeeds.
        
        For example, MecanumDriveWheelSpeeds{2.0, 2.5, 1.5, 1.0} / 2 =
        MecanumDriveWheelSpeeds{1.0, 1.25, 0.75, 0.5}
        
        :param scalar: The scalar to divide by.
        
        :returns: The scaled MecanumDriveWheelSpeeds.
        """
    def desaturate(self, attainableMaxSpeed: wpimath_download.units.meters_per_second) -> None:
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.
        
        Sometimes, after inverse kinematics, the requested speed from one or
        more wheels may be above the max attainable speed for the driving motor on
        that wheel. To fix this issue, one can reduce all the wheel speeds to make
        sure that all requested module speeds are at-or-below the absolute
        threshold, while maintaining the ratio of speeds between wheels.
        
        :param attainableMaxSpeed: The absolute max speed that a wheel can reach.
        """
    @property
    def frontLeft(self) -> wpimath_download.units.meters_per_second:
        """
        Speed of the front-left wheel.
        """
    @frontLeft.setter
    def frontLeft(self, arg0: wpimath_download.units.meters_per_second) -> None:
        ...
    @property
    def frontRight(self) -> wpimath_download.units.meters_per_second:
        """
        Speed of the front-right wheel.
        """
    @frontRight.setter
    def frontRight(self, arg0: wpimath_download.units.meters_per_second) -> None:
        ...
    @property
    def rearLeft(self) -> wpimath_download.units.meters_per_second:
        """
        Speed of the rear-left wheel.
        """
    @rearLeft.setter
    def rearLeft(self, arg0: wpimath_download.units.meters_per_second) -> None:
        ...
    @property
    def rearRight(self) -> wpimath_download.units.meters_per_second:
        """
        Speed of the rear-right wheel.
        """
    @rearRight.setter
    def rearRight(self, arg0: wpimath_download.units.meters_per_second) -> None:
        ...
class SwerveDrive2Kinematics(SwerveDrive2KinematicsBase):
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual module states (speed and angle).
    
    The inverse kinematics (converting from a desired chassis velocity to
    individual module states) uses the relative locations of the modules with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.
    
    Forward kinematics (converting an array of module states into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.
    
    The inverse kinematics: [moduleStates] = [moduleLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [moduleLocations] and then
    multiply by [moduleStates] to get our chassis speeds.
    
    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    @staticmethod
    @typing.overload
    def desaturateWheelSpeeds(moduleStates: tuple[SwerveModuleState, SwerveModuleState], attainableMaxSpeed: wpimath_download.units.meters_per_second) -> tuple[SwerveModuleState, SwerveModuleState]:
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.
        
        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.
        
        :param moduleStates:       Reference to array of module states. The array will be
                                   mutated with the normalized speeds!
        :param attainableMaxSpeed: The absolute max speed that a module can reach.
        """
    @staticmethod
    @typing.overload
    def desaturateWheelSpeeds(moduleStates: tuple[SwerveModuleState, SwerveModuleState], desiredChassisSpeed: ChassisSpeeds, attainableMaxModuleSpeed: wpimath_download.units.meters_per_second, attainableMaxRobotTranslationSpeed: wpimath_download.units.meters_per_second, attainableMaxRobotRotationSpeed: wpimath_download.units.radians_per_second) -> tuple[SwerveModuleState, SwerveModuleState]:
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum, as well as getting rid of joystick saturation at edges
        of joystick.
        
        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.
        
        :param moduleStates:                       Reference to array of module states. The array will be
                                                   mutated with the normalized speeds!
        :param desiredChassisSpeed:                The desired speed of the robot
        :param attainableMaxModuleSpeed:           The absolute max speed a module can reach
        :param attainableMaxRobotTranslationSpeed: The absolute max speed the robot
                                                   can reach while translating
        :param attainableMaxRobotRotationSpeed:    The absolute max speed the robot can
                                                   reach while rotating
        """
    def __init__(self, arg0: wpimath_download.geometry._geometry.Translation2d, arg1: wpimath_download.geometry._geometry.Translation2d) -> None:
        ...
    def resetHeadings(self, moduleHeadings: tuple[wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d]) -> None:
        """
        Reset the internal swerve module headings.
        
        :param moduleHeadings: The swerve module headings. The order of the module
                               headings should be same as passed into the constructor of this class.
        """
    def toChassisSpeeds(self, moduleStates: tuple[SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis state from the
        given module states. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed and
        angle of each module on the robot.
        
        :param moduleStates: The state of the modules as an wpi::array of type
                             SwerveModuleState, NumModules long as measured from respective encoders
                             and gyros. The order of the swerve module states should be same as passed
                             into the constructor of this class.
        
        :returns: The resulting chassis speed.
        """
    def toSwerveModuleStates(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath_download.geometry._geometry.Translation2d = ...) -> tuple[SwerveModuleState, SwerveModuleState]:
        """
        Performs inverse kinematics to return the module states from a desired
        chassis velocity. This method is often used to convert joystick values into
        module speeds and angles.
        
        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.
        
        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
         center of rotation at one corner of the robot and provide a chassis speed
         that only has a dtheta component, the robot will rotate around that corner.
        
        :returns: An array containing the module states. Use caution because these
                  module states are not normalized. Sometimes, a user input may cause one of
                  the module speeds to go above the attainable max velocity. Use the
                  :meth:`desaturateWheelSpeeds` function to rectify this issue.
                  In addition, you can use Python unpacking syntax
                  to directly assign the module states to variables::
        
                    fl, fr, bl, br = kinematics.toSwerveModuleStates(chassisSpeeds)
        """
    def toTwist2d(self, moduleDeltas: tuple[SwerveModulePosition, SwerveModulePosition]) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the
        given module position deltas. This method is often used for odometry --
        determining the robot's position on the field using data from the
        real-world position delta and angle of each module on the robot.
        
        :param moduleDeltas: The latest change in position of the modules (as a
                             SwerveModulePosition type) as measured from respective encoders and gyros.
                             The order of the swerve module states should be same as passed into the
                             constructor of this class.
        
        :returns: The resulting Twist2d.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> tuple[SwerveModuleState, SwerveModuleState]:
        ...
class SwerveDrive2KinematicsBase:
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual wheel speeds. Robot code should not use this directly-
    Instead, use the particular type for your drivetrain (e.g.,
    DifferentialDriveKinematics).
    
    Inverse kinematics converts a desired chassis speed into wheel speeds whereas
    forward kinematics converts wheel speeds into chassis speed.
    """
    def __init__(self) -> None:
        ...
    def toChassisSpeeds(self, wheelSpeeds: tuple[SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis speed from the
        wheel speeds. This method is often used for odometry -- determining the
        robot's position on the field using data from the real-world speed of each
        wheel on the robot.
        
        :param wheelSpeeds: The speeds of the wheels.
        
        :returns: The chassis speed.
        """
    def toTwist2d(self, start: SwerveDrive2WheelPositions, end: SwerveDrive2WheelPositions) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the given
        change in wheel positions. This method is often used for odometry --
        determining the robot's position on the field using changes in the distance
        driven by each wheel on the robot.
        
        :param start: The starting distances driven by the wheels.
        :param end:   The ending distances driven by the wheels.
        
        :returns: The resulting Twist2d in the robot's movement.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> tuple[SwerveModuleState, SwerveModuleState]:
        """
        Performs inverse kinematics to return the wheel speeds from a desired
        chassis velocity. This method is often used to convert joystick values into
        wheel speeds.
        
        :param chassisSpeeds: The desired chassis speed.
        
        :returns: The wheel speeds.
        """
class SwerveDrive2Odometry(SwerveDrive2OdometryBase):
    """
    Class for swerve drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    swerve drive encoders and swerve azimuth encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: SwerveDrive2Kinematics, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition], initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs a SwerveDriveOdometry object.
        
        :param kinematics:      The swerve drive kinematics for your drivetrain.
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The wheel positions reported by each module.
        :param initialPose:     The starting position of the robot on the field.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition], pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The wheel positions reported by each module.
        :param pose:            The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition]) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This also takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics.
        
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The current position of all swerve modules. Please
                                provide the positions in the same order in which you instantiated your
                                SwerveDriveKinematics.
        
        :returns: The new pose of the robot.
        """
class SwerveDrive2OdometryBase:
    """
    Class for odometry. Robot code should not use this directly- Instead, use the
    particular type for your drivetrain (e.g., DifferentialDriveOdometry).
    Odometry allows you to track the robot's position on the field over a course
    of a match using readings from your wheel encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    
    @tparam WheelSpeeds Wheel speeds type.
    @tparam WheelPositions Wheel positions type.
    """
    def __init__(self, kinematics: SwerveDrive2KinematicsBase, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive2WheelPositions, initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs an Odometry object.
        
        :param kinematics:     The kinematics for your drivetrain.
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param initialPose:    The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Returns the position of the robot on the field.
        
        :returns: The pose of the robot.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive2WheelPositions, pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param pose:           The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive2WheelPositions) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics, in addition to the current distance measurement at each wheel.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        
        :returns: The new pose of the robot.
        """
class SwerveDrive2WheelPositions:
    """
    Represents the wheel positions for a swerve drive drivetrain.
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: SwerveDrive2WheelPositions) -> bool:
        """
        Checks equality between this SwerveDriveWheelPositions and another object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are equal.
        """
    def __init__(self, positions: tuple[SwerveModulePosition, SwerveModulePosition]) -> None:
        ...
    def __ne__(self, arg0: SwerveDrive2WheelPositions) -> bool:
        """
        Checks inequality between this SwerveDriveWheelPositions and another
        object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are not equal.
        """
    def interpolate(self, endValue: SwerveDrive2WheelPositions, t: float) -> SwerveDrive2WheelPositions:
        ...
    @property
    def positions(self) -> tuple[SwerveModulePosition, SwerveModulePosition]:
        """
        The distances driven by the wheels.
        """
    @positions.setter
    def positions(self, arg0: tuple[SwerveModulePosition, SwerveModulePosition]) -> None:
        ...
class SwerveDrive3Kinematics(SwerveDrive3KinematicsBase):
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual module states (speed and angle).
    
    The inverse kinematics (converting from a desired chassis velocity to
    individual module states) uses the relative locations of the modules with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.
    
    Forward kinematics (converting an array of module states into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.
    
    The inverse kinematics: [moduleStates] = [moduleLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [moduleLocations] and then
    multiply by [moduleStates] to get our chassis speeds.
    
    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    @staticmethod
    @typing.overload
    def desaturateWheelSpeeds(moduleStates: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState], attainableMaxSpeed: wpimath_download.units.meters_per_second) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.
        
        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.
        
        :param moduleStates:       Reference to array of module states. The array will be
                                   mutated with the normalized speeds!
        :param attainableMaxSpeed: The absolute max speed that a module can reach.
        """
    @staticmethod
    @typing.overload
    def desaturateWheelSpeeds(moduleStates: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState], desiredChassisSpeed: ChassisSpeeds, attainableMaxModuleSpeed: wpimath_download.units.meters_per_second, attainableMaxRobotTranslationSpeed: wpimath_download.units.meters_per_second, attainableMaxRobotRotationSpeed: wpimath_download.units.radians_per_second) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum, as well as getting rid of joystick saturation at edges
        of joystick.
        
        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.
        
        :param moduleStates:                       Reference to array of module states. The array will be
                                                   mutated with the normalized speeds!
        :param desiredChassisSpeed:                The desired speed of the robot
        :param attainableMaxModuleSpeed:           The absolute max speed a module can reach
        :param attainableMaxRobotTranslationSpeed: The absolute max speed the robot
                                                   can reach while translating
        :param attainableMaxRobotRotationSpeed:    The absolute max speed the robot can
                                                   reach while rotating
        """
    def __init__(self, arg0: wpimath_download.geometry._geometry.Translation2d, arg1: wpimath_download.geometry._geometry.Translation2d, arg2: wpimath_download.geometry._geometry.Translation2d) -> None:
        ...
    def resetHeadings(self, moduleHeadings: tuple[wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d]) -> None:
        """
        Reset the internal swerve module headings.
        
        :param moduleHeadings: The swerve module headings. The order of the module
                               headings should be same as passed into the constructor of this class.
        """
    def toChassisSpeeds(self, moduleStates: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis state from the
        given module states. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed and
        angle of each module on the robot.
        
        :param moduleStates: The state of the modules as an wpi::array of type
                             SwerveModuleState, NumModules long as measured from respective encoders
                             and gyros. The order of the swerve module states should be same as passed
                             into the constructor of this class.
        
        :returns: The resulting chassis speed.
        """
    def toSwerveModuleStates(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath_download.geometry._geometry.Translation2d = ...) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Performs inverse kinematics to return the module states from a desired
        chassis velocity. This method is often used to convert joystick values into
        module speeds and angles.
        
        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.
        
        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
         center of rotation at one corner of the robot and provide a chassis speed
         that only has a dtheta component, the robot will rotate around that corner.
        
        :returns: An array containing the module states. Use caution because these
                  module states are not normalized. Sometimes, a user input may cause one of
                  the module speeds to go above the attainable max velocity. Use the
                  :meth:`desaturateWheelSpeeds` function to rectify this issue.
                  In addition, you can use Python unpacking syntax
                  to directly assign the module states to variables::
        
                    fl, fr, bl, br = kinematics.toSwerveModuleStates(chassisSpeeds)
        """
    def toTwist2d(self, moduleDeltas: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the
        given module position deltas. This method is often used for odometry --
        determining the robot's position on the field using data from the
        real-world position delta and angle of each module on the robot.
        
        :param moduleDeltas: The latest change in position of the modules (as a
                             SwerveModulePosition type) as measured from respective encoders and gyros.
                             The order of the swerve module states should be same as passed into the
                             constructor of this class.
        
        :returns: The resulting Twist2d.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        ...
class SwerveDrive3KinematicsBase:
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual wheel speeds. Robot code should not use this directly-
    Instead, use the particular type for your drivetrain (e.g.,
    DifferentialDriveKinematics).
    
    Inverse kinematics converts a desired chassis speed into wheel speeds whereas
    forward kinematics converts wheel speeds into chassis speed.
    """
    def __init__(self) -> None:
        ...
    def toChassisSpeeds(self, wheelSpeeds: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis speed from the
        wheel speeds. This method is often used for odometry -- determining the
        robot's position on the field using data from the real-world speed of each
        wheel on the robot.
        
        :param wheelSpeeds: The speeds of the wheels.
        
        :returns: The chassis speed.
        """
    def toTwist2d(self, start: SwerveDrive3WheelPositions, end: SwerveDrive3WheelPositions) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the given
        change in wheel positions. This method is often used for odometry --
        determining the robot's position on the field using changes in the distance
        driven by each wheel on the robot.
        
        :param start: The starting distances driven by the wheels.
        :param end:   The ending distances driven by the wheels.
        
        :returns: The resulting Twist2d in the robot's movement.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Performs inverse kinematics to return the wheel speeds from a desired
        chassis velocity. This method is often used to convert joystick values into
        wheel speeds.
        
        :param chassisSpeeds: The desired chassis speed.
        
        :returns: The wheel speeds.
        """
class SwerveDrive3Odometry(SwerveDrive3OdometryBase):
    """
    Class for swerve drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    swerve drive encoders and swerve azimuth encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: SwerveDrive3Kinematics, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition], initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs a SwerveDriveOdometry object.
        
        :param kinematics:      The swerve drive kinematics for your drivetrain.
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The wheel positions reported by each module.
        :param initialPose:     The starting position of the robot on the field.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition], pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The wheel positions reported by each module.
        :param pose:            The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This also takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics.
        
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The current position of all swerve modules. Please
                                provide the positions in the same order in which you instantiated your
                                SwerveDriveKinematics.
        
        :returns: The new pose of the robot.
        """
class SwerveDrive3OdometryBase:
    """
    Class for odometry. Robot code should not use this directly- Instead, use the
    particular type for your drivetrain (e.g., DifferentialDriveOdometry).
    Odometry allows you to track the robot's position on the field over a course
    of a match using readings from your wheel encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    
    @tparam WheelSpeeds Wheel speeds type.
    @tparam WheelPositions Wheel positions type.
    """
    def __init__(self, kinematics: SwerveDrive3KinematicsBase, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive3WheelPositions, initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs an Odometry object.
        
        :param kinematics:     The kinematics for your drivetrain.
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param initialPose:    The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Returns the position of the robot on the field.
        
        :returns: The pose of the robot.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive3WheelPositions, pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param pose:           The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive3WheelPositions) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics, in addition to the current distance measurement at each wheel.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        
        :returns: The new pose of the robot.
        """
class SwerveDrive3WheelPositions:
    """
    Represents the wheel positions for a swerve drive drivetrain.
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: SwerveDrive3WheelPositions) -> bool:
        """
        Checks equality between this SwerveDriveWheelPositions and another object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are equal.
        """
    def __init__(self, positions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> None:
        ...
    def __ne__(self, arg0: SwerveDrive3WheelPositions) -> bool:
        """
        Checks inequality between this SwerveDriveWheelPositions and another
        object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are not equal.
        """
    def interpolate(self, endValue: SwerveDrive3WheelPositions, t: float) -> SwerveDrive3WheelPositions:
        ...
    @property
    def positions(self) -> tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]:
        """
        The distances driven by the wheels.
        """
    @positions.setter
    def positions(self, arg0: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> None:
        ...
class SwerveDrive4Kinematics(SwerveDrive4KinematicsBase):
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual module states (speed and angle).
    
    The inverse kinematics (converting from a desired chassis velocity to
    individual module states) uses the relative locations of the modules with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.
    
    Forward kinematics (converting an array of module states into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.
    
    The inverse kinematics: [moduleStates] = [moduleLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [moduleLocations] and then
    multiply by [moduleStates] to get our chassis speeds.
    
    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    @staticmethod
    @typing.overload
    def desaturateWheelSpeeds(moduleStates: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState], attainableMaxSpeed: wpimath_download.units.meters_per_second) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.
        
        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.
        
        :param moduleStates:       Reference to array of module states. The array will be
                                   mutated with the normalized speeds!
        :param attainableMaxSpeed: The absolute max speed that a module can reach.
        """
    @staticmethod
    @typing.overload
    def desaturateWheelSpeeds(moduleStates: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState], desiredChassisSpeed: ChassisSpeeds, attainableMaxModuleSpeed: wpimath_download.units.meters_per_second, attainableMaxRobotTranslationSpeed: wpimath_download.units.meters_per_second, attainableMaxRobotRotationSpeed: wpimath_download.units.radians_per_second) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum, as well as getting rid of joystick saturation at edges
        of joystick.
        
        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.
        
        :param moduleStates:                       Reference to array of module states. The array will be
                                                   mutated with the normalized speeds!
        :param desiredChassisSpeed:                The desired speed of the robot
        :param attainableMaxModuleSpeed:           The absolute max speed a module can reach
        :param attainableMaxRobotTranslationSpeed: The absolute max speed the robot
                                                   can reach while translating
        :param attainableMaxRobotRotationSpeed:    The absolute max speed the robot can
                                                   reach while rotating
        """
    def __init__(self, arg0: wpimath_download.geometry._geometry.Translation2d, arg1: wpimath_download.geometry._geometry.Translation2d, arg2: wpimath_download.geometry._geometry.Translation2d, arg3: wpimath_download.geometry._geometry.Translation2d) -> None:
        ...
    def resetHeadings(self, moduleHeadings: tuple[wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d]) -> None:
        """
        Reset the internal swerve module headings.
        
        :param moduleHeadings: The swerve module headings. The order of the module
                               headings should be same as passed into the constructor of this class.
        """
    def toChassisSpeeds(self, moduleStates: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis state from the
        given module states. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed and
        angle of each module on the robot.
        
        :param moduleStates: The state of the modules as an wpi::array of type
                             SwerveModuleState, NumModules long as measured from respective encoders
                             and gyros. The order of the swerve module states should be same as passed
                             into the constructor of this class.
        
        :returns: The resulting chassis speed.
        """
    def toSwerveModuleStates(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath_download.geometry._geometry.Translation2d = ...) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Performs inverse kinematics to return the module states from a desired
        chassis velocity. This method is often used to convert joystick values into
        module speeds and angles.
        
        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.
        
        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
         center of rotation at one corner of the robot and provide a chassis speed
         that only has a dtheta component, the robot will rotate around that corner.
        
        :returns: An array containing the module states. Use caution because these
                  module states are not normalized. Sometimes, a user input may cause one of
                  the module speeds to go above the attainable max velocity. Use the
                  :meth:`desaturateWheelSpeeds` function to rectify this issue.
                  In addition, you can use Python unpacking syntax
                  to directly assign the module states to variables::
        
                    fl, fr, bl, br = kinematics.toSwerveModuleStates(chassisSpeeds)
        """
    def toTwist2d(self, moduleDeltas: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the
        given module position deltas. This method is often used for odometry --
        determining the robot's position on the field using data from the
        real-world position delta and angle of each module on the robot.
        
        :param moduleDeltas: The latest change in position of the modules (as a
                             SwerveModulePosition type) as measured from respective encoders and gyros.
                             The order of the swerve module states should be same as passed into the
                             constructor of this class.
        
        :returns: The resulting Twist2d.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        ...
class SwerveDrive4KinematicsBase:
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual wheel speeds. Robot code should not use this directly-
    Instead, use the particular type for your drivetrain (e.g.,
    DifferentialDriveKinematics).
    
    Inverse kinematics converts a desired chassis speed into wheel speeds whereas
    forward kinematics converts wheel speeds into chassis speed.
    """
    def __init__(self) -> None:
        ...
    def toChassisSpeeds(self, wheelSpeeds: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis speed from the
        wheel speeds. This method is often used for odometry -- determining the
        robot's position on the field using data from the real-world speed of each
        wheel on the robot.
        
        :param wheelSpeeds: The speeds of the wheels.
        
        :returns: The chassis speed.
        """
    def toTwist2d(self, start: SwerveDrive4WheelPositions, end: SwerveDrive4WheelPositions) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the given
        change in wheel positions. This method is often used for odometry --
        determining the robot's position on the field using changes in the distance
        driven by each wheel on the robot.
        
        :param start: The starting distances driven by the wheels.
        :param end:   The ending distances driven by the wheels.
        
        :returns: The resulting Twist2d in the robot's movement.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Performs inverse kinematics to return the wheel speeds from a desired
        chassis velocity. This method is often used to convert joystick values into
        wheel speeds.
        
        :param chassisSpeeds: The desired chassis speed.
        
        :returns: The wheel speeds.
        """
class SwerveDrive4Odometry(SwerveDrive4OdometryBase):
    """
    Class for swerve drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    swerve drive encoders and swerve azimuth encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: SwerveDrive4Kinematics, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition], initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs a SwerveDriveOdometry object.
        
        :param kinematics:      The swerve drive kinematics for your drivetrain.
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The wheel positions reported by each module.
        :param initialPose:     The starting position of the robot on the field.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition], pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The wheel positions reported by each module.
        :param pose:            The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This also takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics.
        
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The current position of all swerve modules. Please
                                provide the positions in the same order in which you instantiated your
                                SwerveDriveKinematics.
        
        :returns: The new pose of the robot.
        """
class SwerveDrive4OdometryBase:
    """
    Class for odometry. Robot code should not use this directly- Instead, use the
    particular type for your drivetrain (e.g., DifferentialDriveOdometry).
    Odometry allows you to track the robot's position on the field over a course
    of a match using readings from your wheel encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    
    @tparam WheelSpeeds Wheel speeds type.
    @tparam WheelPositions Wheel positions type.
    """
    def __init__(self, kinematics: SwerveDrive4KinematicsBase, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive4WheelPositions, initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs an Odometry object.
        
        :param kinematics:     The kinematics for your drivetrain.
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param initialPose:    The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Returns the position of the robot on the field.
        
        :returns: The pose of the robot.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive4WheelPositions, pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param pose:           The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive4WheelPositions) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics, in addition to the current distance measurement at each wheel.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        
        :returns: The new pose of the robot.
        """
class SwerveDrive4WheelPositions:
    """
    Represents the wheel positions for a swerve drive drivetrain.
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: SwerveDrive4WheelPositions) -> bool:
        """
        Checks equality between this SwerveDriveWheelPositions and another object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are equal.
        """
    def __init__(self, positions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> None:
        ...
    def __ne__(self, arg0: SwerveDrive4WheelPositions) -> bool:
        """
        Checks inequality between this SwerveDriveWheelPositions and another
        object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are not equal.
        """
    def interpolate(self, endValue: SwerveDrive4WheelPositions, t: float) -> SwerveDrive4WheelPositions:
        ...
    @property
    def positions(self) -> tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]:
        """
        The distances driven by the wheels.
        """
    @positions.setter
    def positions(self, arg0: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> None:
        ...
class SwerveDrive6Kinematics(SwerveDrive6KinematicsBase):
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual module states (speed and angle).
    
    The inverse kinematics (converting from a desired chassis velocity to
    individual module states) uses the relative locations of the modules with
    respect to the center of rotation. The center of rotation for inverse
    kinematics is also variable. This means that you can set your set your center
    of rotation in a corner of the robot to perform special evasion maneuvers.
    
    Forward kinematics (converting an array of module states into the overall
    chassis motion) is performs the exact opposite of what inverse kinematics
    does. Since this is an overdetermined system (more equations than variables),
    we use a least-squares approximation.
    
    The inverse kinematics: [moduleStates] = [moduleLocations] * [chassisSpeeds]
    We take the Moore-Penrose pseudoinverse of [moduleLocations] and then
    multiply by [moduleStates] to get our chassis speeds.
    
    Forward kinematics is also used for odometry -- determining the position of
    the robot on the field using encoders and a gyro.
    """
    @staticmethod
    @typing.overload
    def desaturateWheelSpeeds(moduleStates: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState], attainableMaxSpeed: wpimath_download.units.meters_per_second) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum.
        
        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.
        
        :param moduleStates:       Reference to array of module states. The array will be
                                   mutated with the normalized speeds!
        :param attainableMaxSpeed: The absolute max speed that a module can reach.
        """
    @staticmethod
    @typing.overload
    def desaturateWheelSpeeds(moduleStates: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState], desiredChassisSpeed: ChassisSpeeds, attainableMaxModuleSpeed: wpimath_download.units.meters_per_second, attainableMaxRobotTranslationSpeed: wpimath_download.units.meters_per_second, attainableMaxRobotRotationSpeed: wpimath_download.units.radians_per_second) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Renormalizes the wheel speeds if any individual speed is above the
        specified maximum, as well as getting rid of joystick saturation at edges
        of joystick.
        
        Sometimes, after inverse kinematics, the requested speed
        from one or more modules may be above the max attainable speed for the
        driving motor on that module. To fix this issue, one can reduce all the
        wheel speeds to make sure that all requested module speeds are at-or-below
        the absolute threshold, while maintaining the ratio of speeds between
        modules.
        
        :param moduleStates:                       Reference to array of module states. The array will be
                                                   mutated with the normalized speeds!
        :param desiredChassisSpeed:                The desired speed of the robot
        :param attainableMaxModuleSpeed:           The absolute max speed a module can reach
        :param attainableMaxRobotTranslationSpeed: The absolute max speed the robot
                                                   can reach while translating
        :param attainableMaxRobotRotationSpeed:    The absolute max speed the robot can
                                                   reach while rotating
        """
    def __init__(self, arg0: wpimath_download.geometry._geometry.Translation2d, arg1: wpimath_download.geometry._geometry.Translation2d, arg2: wpimath_download.geometry._geometry.Translation2d, arg3: wpimath_download.geometry._geometry.Translation2d, arg4: wpimath_download.geometry._geometry.Translation2d, arg5: wpimath_download.geometry._geometry.Translation2d) -> None:
        ...
    def resetHeadings(self, moduleHeadings: tuple[wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d, wpimath_download.geometry._geometry.Rotation2d]) -> None:
        """
        Reset the internal swerve module headings.
        
        :param moduleHeadings: The swerve module headings. The order of the module
                               headings should be same as passed into the constructor of this class.
        """
    def toChassisSpeeds(self, moduleStates: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis state from the
        given module states. This method is often used for odometry -- determining
        the robot's position on the field using data from the real-world speed and
        angle of each module on the robot.
        
        :param moduleStates: The state of the modules as an wpi::array of type
                             SwerveModuleState, NumModules long as measured from respective encoders
                             and gyros. The order of the swerve module states should be same as passed
                             into the constructor of this class.
        
        :returns: The resulting chassis speed.
        """
    def toSwerveModuleStates(self, chassisSpeeds: ChassisSpeeds, centerOfRotation: wpimath_download.geometry._geometry.Translation2d = ...) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Performs inverse kinematics to return the module states from a desired
        chassis velocity. This method is often used to convert joystick values into
        module speeds and angles.
        
        This function also supports variable centers of rotation. During normal
        operations, the center of rotation is usually the same as the physical
        center of the robot; therefore, the argument is defaulted to that use case.
        However, if you wish to change the center of rotation for evasive
        maneuvers, vision alignment, or for any other use case, you can do so.
        
        :param chassisSpeeds:    The desired chassis speed.
        :param centerOfRotation: The center of rotation. For example, if you set the
         center of rotation at one corner of the robot and provide a chassis speed
         that only has a dtheta component, the robot will rotate around that corner.
        
        :returns: An array containing the module states. Use caution because these
                  module states are not normalized. Sometimes, a user input may cause one of
                  the module speeds to go above the attainable max velocity. Use the
                  :meth:`desaturateWheelSpeeds` function to rectify this issue.
                  In addition, you can use Python unpacking syntax
                  to directly assign the module states to variables::
        
                    fl, fr, bl, br = kinematics.toSwerveModuleStates(chassisSpeeds)
        """
    def toTwist2d(self, moduleDeltas: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the
        given module position deltas. This method is often used for odometry --
        determining the robot's position on the field using data from the
        real-world position delta and angle of each module on the robot.
        
        :param moduleDeltas: The latest change in position of the modules (as a
                             SwerveModulePosition type) as measured from respective encoders and gyros.
                             The order of the swerve module states should be same as passed into the
                             constructor of this class.
        
        :returns: The resulting Twist2d.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        ...
class SwerveDrive6KinematicsBase:
    """
    Helper class that converts a chassis velocity (dx, dy, and dtheta components)
    into individual wheel speeds. Robot code should not use this directly-
    Instead, use the particular type for your drivetrain (e.g.,
    DifferentialDriveKinematics).
    
    Inverse kinematics converts a desired chassis speed into wheel speeds whereas
    forward kinematics converts wheel speeds into chassis speed.
    """
    def __init__(self) -> None:
        ...
    def toChassisSpeeds(self, wheelSpeeds: tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]) -> ChassisSpeeds:
        """
        Performs forward kinematics to return the resulting chassis speed from the
        wheel speeds. This method is often used for odometry -- determining the
        robot's position on the field using data from the real-world speed of each
        wheel on the robot.
        
        :param wheelSpeeds: The speeds of the wheels.
        
        :returns: The chassis speed.
        """
    def toTwist2d(self, start: SwerveDrive6WheelPositions, end: SwerveDrive6WheelPositions) -> wpimath_download.geometry._geometry.Twist2d:
        """
        Performs forward kinematics to return the resulting Twist2d from the given
        change in wheel positions. This method is often used for odometry --
        determining the robot's position on the field using changes in the distance
        driven by each wheel on the robot.
        
        :param start: The starting distances driven by the wheels.
        :param end:   The ending distances driven by the wheels.
        
        :returns: The resulting Twist2d in the robot's movement.
        """
    def toWheelSpeeds(self, chassisSpeeds: ChassisSpeeds) -> tuple[SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState, SwerveModuleState]:
        """
        Performs inverse kinematics to return the wheel speeds from a desired
        chassis velocity. This method is often used to convert joystick values into
        wheel speeds.
        
        :param chassisSpeeds: The desired chassis speed.
        
        :returns: The wheel speeds.
        """
class SwerveDrive6Odometry(SwerveDrive6OdometryBase):
    """
    Class for swerve drive odometry. Odometry allows you to track the robot's
    position on the field over a course of a match using readings from your
    swerve drive encoders and swerve azimuth encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    """
    def __init__(self, kinematics: SwerveDrive6Kinematics, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition], initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs a SwerveDriveOdometry object.
        
        :param kinematics:      The swerve drive kinematics for your drivetrain.
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The wheel positions reported by each module.
        :param initialPose:     The starting position of the robot on the field.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition], pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The wheel positions reported by each module.
        :param pose:            The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, modulePositions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This also takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics.
        
        :param gyroAngle:       The angle reported by the gyroscope.
        :param modulePositions: The current position of all swerve modules. Please
                                provide the positions in the same order in which you instantiated your
                                SwerveDriveKinematics.
        
        :returns: The new pose of the robot.
        """
class SwerveDrive6OdometryBase:
    """
    Class for odometry. Robot code should not use this directly- Instead, use the
    particular type for your drivetrain (e.g., DifferentialDriveOdometry).
    Odometry allows you to track the robot's position on the field over a course
    of a match using readings from your wheel encoders.
    
    Teams can use odometry during the autonomous period for complex tasks like
    path following. Furthermore, odometry can be used for latency compensation
    when using computer-vision systems.
    
    @tparam WheelSpeeds Wheel speeds type.
    @tparam WheelPositions Wheel positions type.
    """
    def __init__(self, kinematics: SwerveDrive6KinematicsBase, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive6WheelPositions, initialPose: wpimath_download.geometry._geometry.Pose2d = ...) -> None:
        """
        Constructs an Odometry object.
        
        :param kinematics:     The kinematics for your drivetrain.
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param initialPose:    The starting position of the robot on the field.
        """
    def getPose(self) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Returns the position of the robot on the field.
        
        :returns: The pose of the robot.
        """
    def resetPosition(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive6WheelPositions, pose: wpimath_download.geometry._geometry.Pose2d) -> None:
        """
        Resets the robot's position on the field.
        
        The gyroscope angle does not need to be reset here on the user's robot
        code. The library automatically takes care of offsetting the gyro angle.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        :param pose:           The position on the field that your robot is at.
        """
    def update(self, gyroAngle: wpimath_download.geometry._geometry.Rotation2d, wheelPositions: SwerveDrive6WheelPositions) -> wpimath_download.geometry._geometry.Pose2d:
        """
        Updates the robot's position on the field using forward kinematics and
        integration of the pose over time. This method takes in an angle parameter
        which is used instead of the angular rate that is calculated from forward
        kinematics, in addition to the current distance measurement at each wheel.
        
        :param gyroAngle:      The angle reported by the gyroscope.
        :param wheelPositions: The current distances measured by each wheel.
        
        :returns: The new pose of the robot.
        """
class SwerveDrive6WheelPositions:
    """
    Represents the wheel positions for a swerve drive drivetrain.
    """
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: SwerveDrive6WheelPositions) -> bool:
        """
        Checks equality between this SwerveDriveWheelPositions and another object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are equal.
        """
    def __init__(self, positions: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> None:
        ...
    def __ne__(self, arg0: SwerveDrive6WheelPositions) -> bool:
        """
        Checks inequality between this SwerveDriveWheelPositions and another
        object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are not equal.
        """
    def interpolate(self, endValue: SwerveDrive6WheelPositions, t: float) -> SwerveDrive6WheelPositions:
        ...
    @property
    def positions(self) -> tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]:
        """
        The distances driven by the wheels.
        """
    @positions.setter
    def positions(self, arg0: tuple[SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition, SwerveModulePosition]) -> None:
        ...
class SwerveModulePosition:
    """
    Represents the position of one swerve module.
    """
    WPIStruct: typing.ClassVar[typing.Any]  # value = <capsule object "WPyStruct" at 0x000002A5EF69FBA0>
    __hash__: typing.ClassVar[None] = None
    distance_ft: wpimath_download.units.feet
    def __eq__(self, arg0: SwerveModulePosition) -> bool:
        """
        Checks equality between this SwerveModulePosition and another object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are equal.
        """
    def __init__(self, distance: wpimath_download.units.meters = 0, angle: wpimath_download.geometry._geometry.Rotation2d = ...) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def interpolate(self, endValue: SwerveModulePosition, t: float) -> SwerveModulePosition:
        ...
    @property
    def angle(self) -> wpimath_download.geometry._geometry.Rotation2d:
        """
        Angle of the module.
        """
    @angle.setter
    def angle(self, arg0: wpimath_download.geometry._geometry.Rotation2d) -> None:
        ...
    @property
    def distance(self) -> wpimath_download.units.meters:
        """
        Distance the wheel of a module has traveled
        """
    @distance.setter
    def distance(self, arg0: wpimath_download.units.meters) -> None:
        ...
class SwerveModuleState:
    """
    Represents the state of one swerve module.
    """
    WPIStruct: typing.ClassVar[typing.Any]  # value = <capsule object "WPyStruct" at 0x000002A5EF69F390>
    __hash__: typing.ClassVar[None] = None
    speed_fps: wpimath_download.units.feet_per_second
    @staticmethod
    def optimize(desiredState: SwerveModuleState, currentAngle: wpimath_download.geometry._geometry.Rotation2d) -> SwerveModuleState:
        """
        Minimize the change in heading the desired swerve module state would
        require by potentially reversing the direction the wheel spins. If this is
        used with the PIDController class's continuous input functionality, the
        furthest a wheel will ever rotate is 90 degrees.
        
        :param desiredState: The desired state.
        :param currentAngle: The current module angle.
        """
    def __eq__(self, arg0: SwerveModuleState) -> bool:
        """
        Checks equality between this SwerveModuleState and another object.
        
        :param other: The other object.
        
        :returns: Whether the two objects are equal.
        """
    def __init__(self, speed: wpimath_download.units.meters_per_second = 0, angle: wpimath_download.geometry._geometry.Rotation2d = ...) -> None:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def angle(self) -> wpimath_download.geometry._geometry.Rotation2d:
        """
        Angle of the module.
        """
    @angle.setter
    def angle(self, arg0: wpimath_download.geometry._geometry.Rotation2d) -> None:
        ...
    @property
    def speed(self) -> wpimath_download.units.meters_per_second:
        """
        Speed of the wheel of the module.
        """
    @speed.setter
    def speed(self, arg0: wpimath_download.units.meters_per_second) -> None:
        ...
