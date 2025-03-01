# MyUtils

Different utilities for general purpose usage on python projects.  

## Authors
> Jaime Alvarez Diaz  
> [![email](https://img.shields.io/static/v1.svg?label=Gmail&message=alvarez.diaz.jaime1@gmail.com&logo=gmail&color=08851b&logoColor=white&colorA=c71610)](mailto:alvarez.diaz.jaime1@gmail.com)  
[![GitHub Profile](https://img.shields.io/static/v1.svg?label=GitHub&message=Jaimead7&logo=github&color=2dba4e&colorA=2b3137)](https://github.com/Jaimead7)  

## Installation
Install as a package
```powershell
git clone https://github.com/Jaimead7/MyUtils
cd MyUtils
py -m pip install wheel tomli
py setup.py bdist_wheel sdist
py -m pip install .
cd ..
rm -r MyUtils
```

## Usage

### Config file
#### PATH's
Default <code>APPLICATIONPATH</code> is <code>../\<main>.py</code> when executed <code>py \<main>.py</code>.  
Default <code>DISTPATH</code> is <code>APPLICATIONPATH/dist</code>  
Default <code>CONFIGPATH</code> is <code>APPLICATIONPATH/dist/config</code>  
In order to work with the default vars config your project with the following structure.  
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

#### config.toml
Base config file should contain <code>[app]</code> section and 
```toml
[app]
    name = 'MyApp'
    version = '0.0.1'
    ...
```
```python
from MyUtils.config import APPLICATIONPATH, CONFIGPATH, DISTPATH, ConfigFileManager, cfg

print(config.app.name)
print(config.app.version)
```
```
>> MyApp
>> 0.0.1
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
from MyUtils.logs import Styles, criticalLog, debugLog, errorLog, infoLog, setLoggingLevel, warningLog

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
from MyUtils.immutable import Immutable

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
from MyUtils.noInstantiable import NoInstantiable

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
from MyUtils.validation import ValidationClass

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