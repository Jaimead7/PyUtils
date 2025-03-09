### NoInstantiable
```python
from pyUtils.noInstantiable import NoInstantiable

class MyClass(NoInstantiable):
    ...

MyClass.func()
myObj = MyClass()
```
```
>> SyntaxError: Class MyClass is not instantiable
```
