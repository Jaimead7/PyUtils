import time
from functools import wraps
from typing import Any, Callable, Optional, TypeVar, Union, cast

from .logs import MyLogger

myLogger: MyLogger = MyLogger(__name__)

F = TypeVar('F', bound= Callable[..., Any])

def timeMe(
    _func: Optional[F] = None,
    *,
    debug: bool = True
) -> Union[Callable[[F], F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start: float = time.time()
            result: Any = func(*args, **kwargs)
            end: float = time.time()
            if debug:
                myLogger.debugLog(f'"{func.__name__}" execution time: {end - start:.4f}s.')
            return result
        return cast(F, wrapper)
    if _func is None:
        return decorator
    return decorator(_func)
