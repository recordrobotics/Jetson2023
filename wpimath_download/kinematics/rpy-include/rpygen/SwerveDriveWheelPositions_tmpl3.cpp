// This file is autogenerated. DO NOT EDIT
#include <robotpy_build.h>




#include <frc\kinematics\SwerveDriveWheelPositions.h>


#include <wpi_array_type_caster.h>



#include <pybind11/operators.h>






#include <rpygen/frc__SwerveDriveWheelPositions.hpp>
#include "SwerveDriveWheelPositions_tmpl.hpp"

namespace rpygen {

using BindType = rpygen::bind_frc__SwerveDriveWheelPositions<4>;
static std::unique_ptr<BindType> inst;

bind_frc__SwerveDriveWheelPositions_2::bind_frc__SwerveDriveWheelPositions_2(py::module &m, const char * clsName)
{
    inst = std::make_unique<BindType>(m, clsName);
}

void bind_frc__SwerveDriveWheelPositions_2::finish(const char *set_doc, const char *add_doc)
{
    inst->finish(set_doc, add_doc);
    inst.reset();
}

}; // namespace rpygen
