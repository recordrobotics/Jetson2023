// This file is autogenerated. DO NOT EDIT
#include <robotpy_build.h>




#include <frc\trajectory\TrapezoidProfile.h>


#include <units_angle_type_caster.h>

#include <units_angular_acceleration_type_caster.h>

#include <units_angular_velocity_type_caster.h>

#include <units_compound_type_caster.h>

#include <units_misc_type_caster.h>

#include <units_time_type_caster.h>



#include <pybind11/operators.h>






#include <rpygen/frc__TrapezoidProfile.hpp>
#include "TrapezoidProfile_tmpl.hpp"

namespace rpygen {

using BindType = rpygen::bind_frc__TrapezoidProfile<units::dimensionless::scalar>;
static std::unique_ptr<BindType> inst;

bind_frc__TrapezoidProfile_0::bind_frc__TrapezoidProfile_0(py::module &m, const char * clsName)
{
    inst = std::make_unique<BindType>(m, clsName);
}

void bind_frc__TrapezoidProfile_0::finish(const char *set_doc, const char *add_doc)
{
    inst->finish(set_doc, add_doc);
    inst.reset();
}

}; // namespace rpygen
