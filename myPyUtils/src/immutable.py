from typing import Any


class Immutable(type):
    """Class with attributes that can't be changed"""
    def __setattr__(self, __name: str, __value: Any) -> None:
        raise SyntaxError(f'Class "{self.__name__}" is immutable')
