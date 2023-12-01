"""
https://adventofcode.com/2023/day/16
"""
from time import perf_counter_ns
from functools import wraps

from task_input import task_input


def timeit(func):

    @wraps(func)
    def decorator(*args, **kwargs):
        start = perf_counter_ns()
        func(*args, **kwargs)
        end = perf_counter_ns()
        ms = (end - start) / 1000 / 1000
        print(f'{ms:.1f} ms')

    return decorator


@timeit
def part_1() -> None:
    """Solution to part 1."""
    ...


@timeit
def part_2() -> None:
    """Solution to part 2."""
    ...


if __name__ == '__main__':
    part_1()
    part_2()
