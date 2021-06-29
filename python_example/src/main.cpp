#include <pybind11/pybind11.h>
namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(python_example, m) {
    m.def("add", &add, "add two ints");
    m.def("subtract", [](int i, int j) { return i - j; }, "subtract two ints");
}
