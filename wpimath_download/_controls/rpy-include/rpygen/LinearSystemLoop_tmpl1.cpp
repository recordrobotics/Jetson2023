// This file is autogenerated. DO NOT EDIT
#include <robotpy_build.h>




#include <frc\system\LinearSystemLoop.h>


#include <pybind11/eigen.h>

#include <pybind11/functional.h>

#include <units_time_type_caster.h>

#include <units_voltage_type_caster.h>








#include <rpygen/frc__LinearSystemLoop.hpp>
#include "LinearSystemLoop_tmpl.hpp"

namespace rpygen {

using BindType = rpygen::bind_frc__LinearSystemLoop<1, 1, 1>;
static std::unique_ptr<BindType> inst;

bind_frc__LinearSystemLoop_0::bind_frc__LinearSystemLoop_0(py::module &m, const char * clsName)
{
    inst = std::make_unique<BindType>(m, clsName);
}

void bind_frc__LinearSystemLoop_0::finish(const char *set_doc, const char *add_doc)
{
    inst->finish(set_doc, add_doc);
    inst.reset();
}

}; // namespace rpygen
