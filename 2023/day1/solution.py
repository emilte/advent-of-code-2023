"""
https://adventofcode.com/2023/day/1
"""

from utils import timeit
from task_input import task_input

digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

digit_keys = digits.keys()


def parse_digit(n: str) -> str:
    return digits[n] if n in digits else n


def scan_first(s: str, i: int = 0) -> str:
    """Find first occurrence of digit in string."""
    c = s[:i]  # Current string to search.

    # Find digit in letters if substring of current search.
    for k in digit_keys:
        ii = c.find(k)
        if ii >= 0:
            return parse_digit(c[ii:])

    if s[i].isdigit():
        # Most recent added string was a digit.
        return s[i]

    # Recursive search.
    return scan_first(s, i + 1)


def scan_last(s: str, i: int = -1) -> str:
    """Find last occurrence of digit in string."""
    c = s[i:]  # Current string to search.

    # Find digit in letters if substring of current search. End-index is unknown -> scan_first.
    for k in digit_keys:
        if k in c:
            return parse_digit(scan_first(c))

    if s[i].isdigit():
        return s[i]

    # Recursive search backwards.
    return scan_last(s, i - 1)


@timeit
def part_1() -> None:
    """Solution to part 1."""
    s = 0
    for t in task_input:
        x: list[str] = [a for a in t if a.isdigit()]
        s += int(x[0] + x[-1])
    print(s)


@timeit
def part_2() -> None:
    """Solution to part 2."""
    s = 0
    for t in task_input:
        s += int(scan_first(t) + scan_last(t))
    print(s)


if __name__ == '__main__':
    part_1()
    part_2()
