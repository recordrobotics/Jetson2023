// This file is autogenerated. DO NOT EDIT
#include <robotpy_build.h>




#include <frc\kinematics\SwerveDriveKinematics.h>


#include <units_angular_velocity_type_caster.h>

#include <units_velocity_type_caster.h>

#include <wpi_array_type_caster.h>







#define RPYGEN_ENABLE_frc__SwerveDriveKinematics_PROTECTED_CONSTRUCTORS
#include <rpygen/frc__SwerveDriveKinematics.hpp>


#include <rpygen/frc__SwerveDriveKinematics.hpp>
#include "SwerveDriveKinematics_tmpl.hpp"

namespace rpygen {

using BindType = rpygen::bind_frc__SwerveDriveKinematics<3>;
static std::unique_ptr<BindType> inst;

bind_frc__SwerveDriveKinematics_1::bind_frc__SwerveDriveKinematics_1(py::module &m, const char * clsName)
{
    inst = std::make_unique<BindType>(m, clsName);
}

void bind_frc__SwerveDriveKinematics_1::finish(const char *set_doc, const char *add_doc)
{
    inst->finish(set_doc, add_doc);
    inst.reset();
}

}; // namespace rpygen
