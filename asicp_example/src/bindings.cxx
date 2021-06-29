#include <pybind11/pybind11.h>
#include <pybind11/eigen.h> // eigen to numpy
#include <pybind11/stl.h> // vector to list

#include "asicp.hxx"

namespace py = pybind11;

using namespace pybind11::literals;

PYBIND11_MODULE(asicp, m) {
    m.def("asicp", &asicp_wrapper, "asicp algorithm", "X"_a, "Y"_a, "threshold"_a=1e-3, "max_iterations"_a=50, "asopa_threshold"_a=1e-8, "rotations"_a=8, "verbose"_a=false);
}
