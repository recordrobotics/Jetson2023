// This file is autogenerated. DO NOT EDIT
#include <robotpy_build.h>




#include <frc\interpolation\TimeInterpolatableBuffer.h>


#include <pybind11/functional.h>

#include <pybind11/stl.h>

#include <units_time_type_caster.h>








#include <rpygen/frc__TimeInterpolatableBuffer.hpp>
#include "TimeInterpolatableBuffer_tmpl.hpp"

namespace rpygen {

using BindType = rpygen::bind_frc__TimeInterpolatableBuffer<double>;
static std::unique_ptr<BindType> inst;

bind_frc__TimeInterpolatableBuffer_6::bind_frc__TimeInterpolatableBuffer_6(py::module &m, const char * clsName)
{
    inst = std::make_unique<BindType>(m, clsName);
}

void bind_frc__TimeInterpolatableBuffer_6::finish(const char *set_doc, const char *add_doc)
{
    inst->finish(set_doc, add_doc);
    inst.reset();
}

}; // namespace rpygen
