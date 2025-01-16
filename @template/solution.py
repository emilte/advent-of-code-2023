"""
https://adventofcode.com/2023/day/<x>
"""

from __future__ import annotations

from time import perf_counter_ns
from typing import Any, Callable
from functools import wraps

from task_input import test1, test2, task_input, task_input2


def timeit(func: Callable) -> Callable:
    @wraps(func)
    def decorator(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter_ns()
        r = func(*args, **kwargs)
        end = perf_counter_ns()
        ms = (end - start) / 1000 / 1000
        print(f'{ms:.1f} ms')
        return r

    return decorator


@timeit
def part_1(task_input: Any) -> None:
    """Solution to part 1."""


@timeit
def part_2(task_input: Any) -> None:
    """Solution to part 2."""


if __name__ == '__main__':
    part_1(test1)
    part_1(task_input)
    part_2(test2)
    part_2(task_input2)
