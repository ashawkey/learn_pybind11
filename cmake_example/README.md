# cmake_example for pybind11

### Installation

Just clone this repository and pip install. Note the `--recursive` option which is
needed for the pybind11 submodule:

```bash
git clone --recursive https://github.com/pybind/cmake_example.git
pip install ./cmake_example
```
### Test call

```python
import cmake_example
cmake_example.add(1, 2)
```
