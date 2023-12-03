"""
https://adventofcode.com/2023/day/3
"""
from math import prod

from utils import timeit
from task_input import task_input, sample


def is_symbol(l: str) -> bool:
    return not l.isdigit() and l != '.'


def scan_symbol(lines: list[str], i: int, j: int) -> bool:
    """Determine if symbol is adjecent."""
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            m = i + y
            n = j + x
            l = lines[m][n]
            if is_symbol(l):
                True
    return False


def find_star(lines: list[str], i: int, j: int) -> tuple[bool, int, int]:
    """Determine location of possible adjecent star."""
    for y in range(-1, 2):
        for x in range(-1, 2):
            if x == 0 and y == 0:
                continue
            m = i + y
            n = j + x
            l = lines[m][n]
            if l == '*':
                return True, m, n
    return False, -1, -1


@timeit
def part_1(task_input) -> None:
    """Solution to part 1."""
    lines = task_input.strip().split('\n')
    border = ['.' * len(lines[0])]
    lines = border + lines + border
    lines = [f'..{line}..' for line in lines]

    s = 0
    for i, line in enumerate(lines):
        n = ''
        keep = False
        for j, l in enumerate(line):

            if l.isdigit():
                n += l
                if scan_symbol(lines, i, j):
                    keep = True

            if n and not l.isdigit():
                if keep:
                    s += int(n)
                n = ''
                keep = False
    print(s)


@timeit
def part_2(task_input) -> None:
    """Solution to part 2."""
    lines = task_input.strip().split('\n')
    border = ['.' * len(lines[0])]
    lines = border + lines + border
    lines = [f'..{line}..' for line in lines]

    d = {}

    for i, line in enumerate(lines):
        n = ''
        yx = ''
        for j, l in enumerate(line):

            if l.isdigit():
                n += l
                found, y, x = find_star(lines, i, j)
                if found:
                    yx = f'{y}-{x}'
                    d.setdefault(yx, [])

            if n and not l.isdigit():
                if yx:
                    d[yx].append(int(n))
                n = ''
                yx = ''

    s = sum([prod(x) for x in d.values() if len(x) == 2])
    print(s)


if __name__ == '__main__':
    part_2(task_input)
    part_2(task_input)
