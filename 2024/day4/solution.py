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
    def decorator(*args: Any, **kwargs: Any) -> None:
        start = perf_counter_ns()
        r = func(*args, **kwargs)
        end = perf_counter_ns()
        ms = (end - start) / 1000 / 1000
        print(f'{ms:.1f} ms')
        return r

    return decorator


def is_mas(s: str) -> bool:
    return s in {'MAS', 'SAM'}


def get_diagonals(matrix):
    n = len(matrix)
    m = len(matrix[0])
    diagonals = []

    # Top-left to bottom-right diagonals
    for d in range(n + m - 1):
        diag1 = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            diag1.append(matrix[i][d - i])
        diagonals.append(''.join(diag1))

    # Top-right to bottom-left diagonals
    for d in range(n + m - 1):
        diag2 = []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            diag2.append(matrix[i][m - 1 - (d - i)])
        diagonals.append(''.join(diag2))

    return diagonals


def extract_diagonals(matrix: list[str]) -> tuple[str, str]:
    n = len(matrix)
    primary_diagonal = ''
    secondary_diagonal = ''

    for i in range(n):
        primary_diagonal += matrix[i][i]
        secondary_diagonal += matrix[i][n - 1 - i]

    return primary_diagonal, secondary_diagonal


@timeit
def part_1(task_input: list[str]) -> None:
    """Solution to part 1."""
    s = 0
    for i in task_input:
        s += i.count('XMAS')
        s += i.count('SAMX')

    transposed = [''.join(row) for row in zip(*task_input)]
    for i in transposed:
        s += i.count('XMAS')
        s += i.count('SAMX')

    d = get_diagonals(task_input)
    for i in d:
        s += i.count('XMAS')
        s += i.count('SAMX')

    print(s)
    return s


def get_3x3_chunks(matrix: list[str]) -> list[list[str]]:
    rows = len(matrix)
    cols = len(matrix[0])
    chunks = []

    for i in range(rows - 2):
        for j in range(cols - 2):
            chunk = [matrix[i + x][j : j + 3] for x in range(3)]
            chunks.append(chunk)

    return chunks


@timeit
def part_2(task_input: Any) -> None:
    """Solution to part 2."""
    chunks = get_3x3_chunks(task_input)
    s = 0
    for chunk in chunks:
        left, right = extract_diagonals(chunk)
        if is_mas(left) and is_mas(right):
            s += 1
    print(s)
    return s


if __name__ == '__main__':
    assert part_1(test1) == 18
    part_1(task_input)
    assert part_2(test2) == 9
    part_2(task_input2)
