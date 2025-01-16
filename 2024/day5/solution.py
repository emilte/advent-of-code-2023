"""
https://adventofcode.com/2023/day/<x>
"""

from __future__ import annotations

from time import perf_counter_ns
from typing import Any, Callable
from functools import wraps

import task_input


def timeit(func: Callable) -> Callable:
    @wraps(func)
    def decorator(*args: Any, **kwargs: Any) -> None:
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
    rules, updates = task_input
    _rules = sorted(rules, key=lambda x: x[1])
    aa = []
    for li, ri in _rules:
        aa.append(li)
        aa.append(ri)

    aa = list(set(aa))
    # aa = sorted(set(aa))

    for l, r in _rules:
        li = aa.index(l)
        ri = aa.index(r)
        if li > ri:
            a = aa.pop(li)
            # aa = [a] + aa
            aa.insert(ri, a)

    # aa = ','.join([str(x) for x in aa])
    s = 0
    for u in updates:
        # k = ','.join([str(x) for x in u])
        x = [a for a in aa if a in u]
        if u == x:
            mi = int((len(u) - 1) / 2)
            s += u[mi]

    print(s)
    return s


@timeit
def part_2(task_input: Any) -> None:
    """Solution to part 2."""


if __name__ == '__main__':
    assert part_1(task_input.test1) == 143
    part_1(task_input.task_input)
    part_2(task_input.test2)
    part_2(task_input.task_input2)
