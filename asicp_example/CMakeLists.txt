cmake_minimum_required(VERSION 3.4)
project(asicp)

set (CMAKE_CXX_STANDARD 17)

find_package(Eigen3 3.3 REQUIRED NO_MODULE)
find_package(nanoflann)

add_definitions(-Ofast -ftree-vectorize -finline-functions -march=native -flto)

aux_source_directory(src SRCS)

add_subdirectory(pybind11)

# replace exe with pybind module
#add_executable(asicp ${SRCS})
pybind11_add_module(asicp ${SRCS})

# must use PRIVATE
target_link_libraries(asicp PRIVATE nanoflann::nanoflann)
target_link_libraries(asicp PRIVATE Eigen3::Eigen)
