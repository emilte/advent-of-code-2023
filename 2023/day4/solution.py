"""
https://adventofcode.com/2023/day/4
"""

from utils import timeit
from task_input import task_input, sample


@timeit
def part_1(task_input: str) -> None:
    """Solution to part 1."""
    lines = task_input.strip().split('\n')
    s = 0
    for line in lines:
        p = 0
        p1, p2 = line.split('|')
        winning_numbers = set(p1.split(':')[1].split())
        card = p2.split()
        for n in card:
            if n in winning_numbers:
                if p == 0:
                    p = 1
                else:
                    p *= 2
        s += p
    print(s)


@timeit
def part_2(task_input: str) -> None:
    """Solution to part 2."""
    lines = task_input.strip().split('\n')
    cmap = {int(line.split()[1][:-1]): line for line in lines}
    for line in lines:

        p1, p2 = line.split('|')
        card_id, winning_numbers = p1.split(':')
        card_id = int(card_id.split()[1])
        winning_numbers = set(winning_numbers.split())
        card = p2.split()
        c = 0
        for n in card:
            if n in winning_numbers:
                c += 1
        for cc in range(c):
            lines.append(cmap[card_id + cc + 1])
    print(len(lines))


if __name__ == '__main__':
    part_1(sample)  # 13
    part_1(task_input)  # 21485
    part_2(sample)  # 30
    # part_2(task_input)  # 11024379
