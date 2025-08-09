### ValidationClass
```python
from pyUtils.validation import ValidationClass

class MyClass(ValidationClass):
    def __init__(self):        
        self.var: float = 5
    
    def validate_var(self, value: Any):
        try:
            return self.validate_float(value)
        except TypeError:
            raise TypeError(f'Invalid type {self.__class__}.var: {value}')

    ...

intVar = ValidationClass.Validate_int('5')
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
