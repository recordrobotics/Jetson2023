

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>



#include <frc\trajectory\TrapezoidProfile.h>










#include <units_angle_type_caster.h>

#include <units_angular_acceleration_type_caster.h>

#include <units_angular_velocity_type_caster.h>

#include <units_compound_type_caster.h>

#include <units_misc_type_caster.h>

#include <units_time_type_caster.h>


namespace rpygen {


using namespace frc;




template <typename Distance>
struct bind_frc__TrapezoidProfile {

    

    
  using Constraints [[maybe_unused]] = typename frc::TrapezoidProfile<Distance>::Constraints;
  
  using State [[maybe_unused]] = typename frc::TrapezoidProfile<Distance>::State;
  
  
  
    using Distance_t [[maybe_unused]] = typename frc::TrapezoidProfile<Distance>::Distance_t;
  
    using Velocity [[maybe_unused]] = typename frc::TrapezoidProfile<Distance>::Velocity;
  
    using Velocity_t [[maybe_unused]] = typename frc::TrapezoidProfile<Distance>::Velocity_t;
  
    using Acceleration [[maybe_unused]] = typename frc::TrapezoidProfile<Distance>::Acceleration;
  
    using Acceleration_t [[maybe_unused]] = typename frc::TrapezoidProfile<Distance>::Acceleration_t;
  

    

    py::class_<typename frc::TrapezoidProfile<Distance>> cls_TrapezoidProfile;

    

    
    
    py::class_<typename frc::TrapezoidProfile<Distance>::Constraints> cls_Constraints;

    

    
    
    
    py::class_<typename frc::TrapezoidProfile<Distance>::State> cls_State;

    

    
    
    

    py::module &m;
    std::string clsName;

bind_frc__TrapezoidProfile(py::module &m, const char * clsName) :
    
    cls_TrapezoidProfile(m, clsName),

  

  
  
    cls_Constraints(cls_TrapezoidProfile, "Constraints"),

  

  
  
  
    cls_State(cls_TrapezoidProfile, "State"),

  

  
  
  
    m(m),
    clsName(clsName)
{
    
  

}

void finish(const char * set_doc = NULL, const char * add_doc = NULL) {

    

  cls_TrapezoidProfile.doc() =
    "A trapezoid-shaped velocity profile.\n"
"\n"
"While this class can be used for a profiled movement from start to finish,\n"
"the intended usage is to filter a reference's dynamics based on trapezoidal\n"
"velocity constraints. To compute the reference obeying this constraint, do\n"
"the following.\n"
"\n"
"Initialization::\n"
"\n"
"  constraints = TrapezoidProfile.Constraints(kMaxV, kMaxA)\n"
"  previousProfiledReference = initialReference\n"
"\n"
"Run on update::\n"
"\n"
"  profile = TrapezoidProfile(constraints, unprofiledReference, previousProfiledReference)\n"
"  previousProfiledReference = profile.calculate(timeSincePreviousUpdate)\n"
"\n"
"where ``unprofiledReference`` is free to change between calls. Note that\n"
"when the unprofiled reference is within the constraints,\n"
":meth:`calculate` returns the unprofiled reference unchanged.\n"
"\n"
"Otherwise, a timer can be started to provide monotonic values for\n"
"``calculate()`` and to determine when the profile has completed via\n"
":meth:`isFinished`.\n";

  cls_TrapezoidProfile
  
    
  .def(py::init<typename TrapezoidProfile<Distance>::Constraints>(),
      py::arg("constraints"), release_gil(), py::doc(
    "Constructs a TrapezoidProfile.\n"
"\n"
":param constraints: The constraints on the profile, like maximum velocity.")
  )
  
  
  
    
  .def(py::init<typename TrapezoidProfile<Distance>::Constraints, typename TrapezoidProfile<Distance>::State, typename TrapezoidProfile<Distance>::State>(),
      py::arg("constraints"), py::arg("goal"), py::arg("initial") = State{Distance_t{0}, Velocity_t{0}}, release_gil(), py::doc(
    "Constructs a TrapezoidProfile.\n"
"\n"
":deprecated: Pass the desired and current state into calculate instead of\n"
"             constructing a new TrapezoidProfile with the desired and current state\n"
"\n"
":param constraints: The constraints on the profile, like maximum velocity.\n"
":param goal:        The desired state when the profile is complete.\n"
":param initial:     The initial state (usually the current state).")
  )
  
  
  
    
  .
def
("calculate", static_cast<State(frc::TrapezoidProfile<Distance>::*)(units::second_t) const>(
        &frc::TrapezoidProfile<Distance>::Calculate),
      py::arg("t"), release_gil(), py::doc(
    "Calculates the position and velocity for the profile at a time t where the\n"
"current state is at time t = 0.\n"
"\n"
":deprecated: Pass the desired and current state into calculate instead of\n"
"             constructing a new TrapezoidProfile with the desired and current state\n"
"\n"
":param t: How long to advance from the current state toward the desired\n"
"          state.\n"
"\n"
":returns: The position and velocity of the profile at time t.")
  )
  
  
  
    
  .
def
("calculate", static_cast<State(frc::TrapezoidProfile<Distance>::*)(units::second_t, State, State)>(
        &frc::TrapezoidProfile<Distance>::Calculate),
      py::arg("t"), py::arg("current"), py::arg("goal"), release_gil(), py::doc(
    "Calculates the position and velocity for the profile at a time t where the\n"
"current state is at time t = 0.\n"
"\n"
":param t:       How long to advance from the current state toward the desired\n"
"                state.\n"
":param current: The current state.\n"
":param goal:    The desired state when the profile is complete.\n"
"\n"
":returns: The position and velocity of the profile at time t.")
  )
  
  
  
    
  .
def
("timeLeftUntil", &frc::TrapezoidProfile<Distance>::TimeLeftUntil,
      py::arg("target"), release_gil(), py::doc(
    "Returns the time left until a target distance in the profile is reached.\n"
"\n"
":param target: The target distance.\n"
"\n"
":returns: The time left until a target distance in the profile is reached.")
  )
  
  
  
    
  .
def
("totalTime", &frc::TrapezoidProfile<Distance>::TotalTime, release_gil(), py::doc(
    "Returns the total time the profile takes to reach the goal.\n"
"\n"
":returns: The total time the profile takes to reach the goal.")
  )
  
  
  
    
  .
def
("isFinished", &frc::TrapezoidProfile<Distance>::IsFinished,
      py::arg("t"), release_gil(), py::doc(
    "Returns true if the profile has reached the goal.\n"
"\n"
"The profile has reached the goal if the time since the profile started has\n"
"exceeded the profile's total time.\n"
"\n"
":param t: The time since the beginning of the profile.\n"
"\n"
":returns: True if the profile has reached the goal.")
  )
  
  
  ;

  


  

  cls_Constraints.doc() =
    "Profile constraints.";

  cls_Constraints
  
    
  .def(py::init<Velocity_t, Acceleration_t>(),
      py::arg("maxVelocity"), py::arg("maxAcceleration"), release_gil(), py::doc(
    "Constructs constraints for a Trapezoid Profile.\n"
"\n"
":param maxVelocity:     Maximum velocity.\n"
":param maxAcceleration: Maximum acceleration.")
  )
  
  
  
    .def_readonly("maxVelocity", &frc::TrapezoidProfile<Distance>::Constraints::maxVelocity, py::doc(
    "Maximum velocity."))
  
    .def_readonly("maxAcceleration", &frc::TrapezoidProfile<Distance>::Constraints::maxAcceleration, py::doc(
    "Maximum acceleration."))
  ;

  


  
  

  cls_State.doc() =
    "Profile state.";

  cls_State
  
    
  .def(py::self == State()
  )
  
  
  
    .def_readonly("position", &frc::TrapezoidProfile<Distance>::State::position, py::doc(
    "The position at this state."))
  
    .def_readonly("velocity", &frc::TrapezoidProfile<Distance>::State::velocity, py::doc(
    "The velocity at this state."))
  ;

  


  

    if (set_doc) {
        cls_TrapezoidProfile.doc() = set_doc;
    }
    if (add_doc) {
        cls_TrapezoidProfile.doc() = py::cast<std::string>(cls_TrapezoidProfile.doc()) + add_doc;
    }

    {
std::string clsNameCopy = clsName;

cls_State
  .def(
    py::init<Distance_t, Velocity_t>(),
    py::arg("position") = 0,
    py::arg("velocity") = 0
  )
  .def("__repr__", [clsNameCopy](const State &self) {
    return clsNameCopy + ".State("
      "position=" + std::to_string(self.position()) + ", "
      "velocity=" + std::to_string(self.velocity()) + ")";
  });
}

}

}; // struct bind_frc__TrapezoidProfile

}; // namespace rpygen
