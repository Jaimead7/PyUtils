from typing import Literal

from pytest import raises

from ..src.noInstantiable import *


class NoInstantiableClass(NoInstantiable):
    def __init__(self) -> None:
        ...

    @staticmethod
    def testFunc() -> Literal[True]:
        return True


class TestNoInstantiable:
    def test_instance(self) -> None:
        with raises(SyntaxError):
            obj = NoInstantiableClass()

    def test_funcCalls(self) -> None:
        assert NoInstantiableClass.testFunc()
