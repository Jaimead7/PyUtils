# MyUtils

Different utilities for general purpose usage on python projects.  

## Authors
> Jaime Alvarez Diaz  
> [![email](https://img.shields.io/static/v1.svg?label=Gmail&message=alvarez.diaz.jaime1@gmail.com&logo=gmail&color=08851b&logoColor=white&colorA=c71610)](mailto:alvarez.diaz.jaime1@gmail.com)  
[![GitHub Profile](https://img.shields.io/static/v1.svg?label=GitHub&message=Jaimead7&logo=github&color=2dba4e&colorA=2b3137)](https://github.com/Jaimead7)  

## Installation
```bash
cd myProject/src/submodules
git submodule add https://github.com/Jaimead7/MyUtils
```

## Usage
```python
from myUtils import *

...
```
### Config file
```python
...
```
### Debug
```python
from myUtils.debug import debug, Styles

debug('Debug message', Styles= Styles.WARNING)
```  
<code>>> <i style= "color: gold">01/01/1900 00:00:00:</i> Debug messsage</code>

### Immutable
```python
from myUtils.immutable import Immutable

class MyClass(metaclass= Immutable):
    ...

myObj = MyClass()
myObj.var = 0
```
<code>>> <i style= "color: red">Syntax error: Class MyClass is immutable</i></code>  

### NoInstantiable
```python
from myUtils.noInstantiable import NoInstantiable

class MyClass(NoInstantiable):
    ...

MyClass.func()
myObj = MyClass()
```
<code>>> <i style= "color: red">Syntax error: Class MyClass is not instantiable</i></code>  

### ValidationClass
```python
from myUtils.validation import ValidationClass

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
```
```
>> <class 'int'>
>> <class 'float'>
>> <class 'float'>
```
```
myObj.var = 'a'
```
<code> >> <i style= "color: red">Syntax error: Class MyClass is not instantiable</i></code>

## Contributing
Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[![License](https://img.shields.io/badge/MIT-2b3137)](LICENSE)  