# MyPyUtils

Different utilities for general purpose usage on python projects.  
<br>
[![Tests indicator](https://github.com/Jaimead7/MyPyUtils/actions/workflows/python310-lint-test.yml/badge.svg)](https://github.com/Jaimead7/MyPyUtils/actions/workflows/python310-lint-test.yml)  
[![License](https://img.shields.io/static/v1.svg?label=LICENSE&message=MIT&color=2dba4e&colorA=2b3137)](https://github.com/Jaimead7/MyPyUtils/blob/master/LICENSE)  
[![PyPI Latest Release](https://img.shields.io/pypi/v/MyPyUtils.svg?color=2dba4e)](https://pypi.org/project/MyPyUtils/)

## Authors
> Jaime Alvarez Diaz  
> [![email](https://img.shields.io/static/v1.svg?label=Gmail&message=alvarez.diaz.jaime1@gmail.com&logo=gmail&color=2dba4e&logoColor=white&colorA=c71610)](mailto:alvarez.diaz.jaime1@gmail.com)  
[![GitHub Profile](https://img.shields.io/static/v1.svg?label=GitHub&message=Jaimead7&logo=github&color=2dba4e&colorA=2b3137)](https://github.com/Jaimead7)  

## Installation
Install as a package from source files
```powershell
git clone https://github.com/Jaimead7/MyPyUtils.git
cd MyPyUtils
py -m pip install wheel tomli
py setup.py bdist_wheel
py -m pip install ./dist/MyPyUtils-x.x.x-py3-none-any.whl
cd ..
rm -r MyPyUtils
```

Install as a package from pypi (not implemented)
```powershell
py -m pip install MyPyUtils
```

## Usage
- [Config](docs/config.md)
- [Immutable](docs/immutable.md)
- [Logs](docs/logs.md)
- [NoInstantiable](docs/noInstantiable.md)
- [ValidationClass](docs/validationClass.md)

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
