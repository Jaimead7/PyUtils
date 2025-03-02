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
