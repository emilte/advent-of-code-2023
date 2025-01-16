"""
https://adventofcode.com/2023/day/<x>
"""

from __future__ import annotations

from time import perf_counter_ns
from typing import Any, Callable
from functools import wraps

from task_input import INPUT


def timeit(func: Callable) -> Callable:
    @wraps(func)
    def decorator(*args: Any, **kwargs: Any) -> None:
        start = perf_counter_ns()
        func(*args, **kwargs)
        end = perf_counter_ns()
        ms = (end - start) / 1000 / 1000
        print(f'{ms:.1f} ms')

    return decorator


@timeit
def part_1() -> None:
    """Solution to part 1."""
    safe = 0
    for report in INPUT:
        is_safe = True
        c = report[0]
        for lvl in report[1:]:
            if comp(c, lvl, desc=True):
                c = lvl
            else:
                is_safe = False
                break
        if is_safe:
            safe += 1
            continue

        is_safe = True
        c = report[0]
        for lvl in report[1:]:
            if comp(c, lvl, desc=False):
                c = lvl
            else:
                is_safe = False
                break
        if is_safe:
            safe += 1
            continue
    print(safe)


def comp(a: int, b: int, *, desc: bool = False) -> bool:
    tol = 1 <= abs(a - b) <= 3
    if desc:
        return a > b and tol
    return a < b and tol


def r(ir: list, *, desc: bool = False) -> bool:
    return all(comp(ir[l - 1], ir[l], desc=desc) for l in range(1, len(ir)))


@timeit
def part_2() -> None:
    """Solution to part 2."""
    s = 0
    for report in INPUT:
        g = range(len(report))
        if any(r(report[:l] + report[l + 1 :], desc=False) for l in g) or any(
            r(report[:l] + report[l + 1 :], desc=True) for l in g
        ):
            s += 1
    print(s)


if __name__ == '__main__':
    part_1()  # 213
    part_2()  # 285
