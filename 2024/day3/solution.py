"""
https://adventofcode.com/2023/day/<x>
"""

from __future__ import annotations

import re
from time import perf_counter_ns
from typing import Any, Callable
from functools import wraps

from task_input import task_input


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
def part_1(input_string: str) -> None:
    """Solution to part 1."""
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, input_string)
    total_sum = 0
    for match in matches:
        x, y = map(int, match)
        total_sum += x * y
    print(total_sum)


@timeit
def part_2(input_string: str) -> None:
    """Solution to part 2."""
    do = 'do()'
    dont = "don't()"
    while True:
        i = input_string.find(dont)
        if i == -1:
            break
        j = input_string[i:].find(do)
        k = j
        if j == -1:
            # Means don't() apply to rest of string.
            void = input_string[i:]
        else:
            # Find section of string between don't() and do().
            k = len(input_string[:i]) + j + len(do)
            assert k > i
            void = input_string[i:k]

        input_string = input_string.replace(void, '', 1)
        if j == -1:
            break
    part_1(input_string)


if __name__ == '__main__':
    part_1(task_input)  # 196826776
    part_2(task_input)  # 106780429
