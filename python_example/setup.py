from setuptools import setup

from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir

import sys
import glob

sources = sorted(glob.glob("src/*.cpp"))

ext_modules = [
    Pybind11Extension("python_example",
        sources,
    ),
]

setup(
    name="python_example",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
