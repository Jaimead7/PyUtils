# MyPyUtils

Different utilities for general purpose usage on python projects.  

## Authors
> Jaime Alvarez Diaz  
> [![email](https://img.shields.io/static/v1.svg?label=Gmail&message=alvarez.diaz.jaime1@gmail.com&logo=gmail&color=08851b&logoColor=white&colorA=c71610)](mailto:alvarez.diaz.jaime1@gmail.com)  
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

### Config file
#### ProjectPathsDict
Dict with validation for paths. On error <code>path = None</code>.  
<code>ppath</code> is an instance of <code>ProjectPathsDict</code> containing default paths.  
Default <code>APPLICATIONPATH</code> is <code>../\<main>.py</code> when executed <code>py \<main>.py</code>.  
Default <code>DISTPATH</code> is <code>APPLICATIONPATH/dist</code>  
Default <code>CONFIGPATH</code> is <code>APPLICATIONPATH/dist/config</code>  

#### ConfigFileManager
Class to manage <code>.toml</code> files  
<code>cfg</code> is an instance of <code>ConfigFileManager</code> for <code>APPLICATIONPATH/dist/config/config.toml</code>  
On error <code>cfg = None</code>

#### Example
Project structure
```
APPLICATIONPATH
├── dist
│   ├── config
│   │   ├── config.toml
│   │   └── ...
│   └── ...
├── src
│   ├── main.py
│   └── ...
└── ...
```
config.toml
```toml
[app]
    name = 'MyApp'
    version = '0.0.1'
    ...
```
main.py
```python
from MyPyUtils.config import ConfigFileManager, ProjectPathsDict, cfg, ppaths


print(ppaths['APPLICATIONPATH'])
print(ppaths['DISTPATH'])
print(ppaths['CONFIGPATH'])
print(ppaths['CONFIGFILEPATH'])

print(cfg.app.name)
print(cfg.app.version)

ppaths.setAppPath(ppaths['DISTPATH'])
print(ppaths['APPLICATIONPATH'])
print(ppaths['DISTPATH'])
print(ppaths['CONFIGPATH'])
print(ppaths['CONFIGFILEPATH'])
```
```
>> C:/.../APPLICATIONPATH
>> C:/.../APPLICATIONPATH/dist
>> C:/.../APPLICATIONPATH/dist/config
>> C:/.../APPLICATIONPATH/dist/config/config.toml
>> MyApp
>> 0.0.1
>> C:/.../APPLICATIONPATH/dist
>> None
>> None
>> None
```

### Logs
<code>loggingLevel</code> can be defined in the <code>config.toml</code> file under the <code>[app]</code> section.  
If it is not defined, the default value is <code>Debug</code>.  
```toml
[app]
    loggingLevel = "Debug"  #[Debug, Info, Warning, Error, Critical]
    ...
```
```python
from MyPyUtils.logs import Styles, criticalLog, debugLog, errorLog, infoLog, setLoggingLevel, warningLog

debugLog('Test debug')
infoLog('Test info')
warningLog('Test warning')
errorLog('Test error')
criticalLog('Test critical')

setLoggingLevel(logging.CRITICAL)

debugLog('Test new debug', style= Styles.PURPLE)
infoLog('Test new info', style= Styles.PURPLE)
warningLog('Test new warning', style= Styles.PURPLE)
errorLog('Test new error', style= Styles.PURPLE)
criticalLog('Test new critical', style= Styles.PURPLE)
```  
```
>> DEBUG -----> 01/03/2025 13:55:42: Test debug1
>> WARNING ---> 01/03/2025 13:55:42: Test warning
>> ERROR -----> 01/03/2025 13:55:42: Test error
>> CRITICAL --> 01/03/2025 13:55:42: Test critical
>> CRITICAL --> 01/03/2025 13:55:42: Test new critical
```
### Immutable
```python
from MyPyUtils.immutable import Immutable

class MyClass(metaclass= Immutable):
    ...

myObj = MyClass()
myObj.var = 0
``` 
```
>> SyntaxError: Class MyClass is immutable
``` 

### NoInstantiable
```python
from MyPyUtils.noInstantiable import NoInstantiable

class MyClass(NoInstantiable):
    ...

MyClass.func()
myObj = MyClass()
```
```
>> SyntaxError: Class MyClass is not instantiable
```

### ValidationClass
```python
from MyPyUtils.validation import ValidationClass

class MyClass(ValidationClass):
    def __init__(self):        
        self.var: float = 5
    
    def validate_var(self, value: Any):
        try:
            return self.validateFloat(value)
        except TypeError:
            raise TypeError(f'Invalid type {self.__class__}.var: {value}')

    ...

intVar = ValidationClass.ValidateInt('5')
print(type(intVar))
myObj = MyClass()
print(type(myObj.var))
myObj.var = '5'
print(type(myObj.var))
myObj.var = 'a'
```
```
>> <class 'int'>
>> <class 'float'>
>> <class 'float'>
>> TypeError: Invalid type MyClass.var: a
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[![License](https://img.shields.io/badge/MIT-2b3137)](LICENSE)  