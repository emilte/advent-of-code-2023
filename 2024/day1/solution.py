"""
https://adventofcode.com/2024/day/1
"""

from __future__ import annotations

from task_input import L1, L2

from utils import timeit

# from aoc.utils import timeit

# from utils import timeit


@timeit
def part_1() -> None:
    """Solution to part 1."""
    l1 = sorted(L1)
    l2 = sorted(L2)
    s = 0
    for i in range(len(l1)):
        s += abs(l1[i] - l2[i])
    print(s)  # 1765812


@timeit
def part_2() -> None:
    """Solution to part 2."""
    c1 = {}
    c2 = {}
    s = 0
    x = set(L1)
    for i in x:
        if i not in c1:
            c1[i] = L1.count(i)

        if i not in c2:
            c2[i] = L2.count(i)

        s += i * c1[i] * c2[i]

    print(s)  # 20520794


if __name__ == '__main__':
    part_1()
    part_2()
