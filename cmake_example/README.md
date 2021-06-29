# cmake_example for pybind11

### Installation

Just clone this repository and pip install. Note the `--recursive` option which is
needed for the pybind11 submodule:

```bash
# if forget --recursive
#git submodule add -b stable https://github.com/pybind/pybind11.git pybind11
#git submodule update --init

python setup.py build_ext --inplace
```
### Test call

```python
import cmake_example
cmake_example.add(1, 2)
```
