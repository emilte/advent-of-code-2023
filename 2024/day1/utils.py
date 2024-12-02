from __future__ import annotations

from time import perf_counter_ns
from typing import Any, Callable
from functools import wraps


def timeit(func: Callable) -> Callable:
    @wraps(func)
    def decorator(*args: Any, **kwargs: Any) -> None:
        start = perf_counter_ns()
        func(*args, **kwargs)
        end = perf_counter_ns()
        ms = (end - start) / 1000 / 1000
        print(f'{ms:.1f} ms')

    return decorator
