"""
https://adventofcode.com/2023/day/2
"""

from utils import timeit
from task_input import task_input

RED = 'red'
GREEN = 'green'
BLUE = 'blue'


@timeit
def part_1(input) -> None:
    """Solution to part 1."""

    limits = {
        RED: 12,
        GREEN: 13,
        BLUE: 14,
    }

    s = 0
    lines = input.strip().split('\n')
    for line in lines:
        # (Game 6: 1 red, 12 blue; 20 blue, 3 green, 2 red; 4 red, 15 blue)
        game, sets_str = line.split(': ', maxsplit=1)
        # (Game 6) (1 red, 12 blue; 20 blue, 3 green, 2 red; 4 red, 15 blue)
        game_id = int(game.split(' ', maxsplit=1)[1])
        sets = sets_str.split(';')  # (1 red, 12 blue) (20 blue, 3 green, 2 red) (4 red, 15 blue)

        valid = True
        for set in sets:
            # (1 red, 12 blue)
            set_cubes = set.strip().split(', ')  # (1 red) (12 blue)

            for cubes in set_cubes:
                c, t = cubes.split(' ')  # (1) (red)

                if int(c) > limits[t]:
                    valid = False
                    break
        if valid:
            s += game_id

    print(s)


@timeit
def part_2(input: str) -> None:
    """Solution to part 2."""
    sum_power = 0
    lines = input.strip().split('\n')
    for line in lines:
        # (Game 6: 1 red, 12 blue; 20 blue, 3 green, 2 red; 4 red, 15 blue)
        sets_str = line.split(': ', maxsplit=1)[1]
        # (1 red, 12 blue; 20 blue, 3 green, 2 red; 4 red, 15 blue)
        sets = sets_str.split(';')  # (1 red, 12 blue) (20 blue, 3 green, 2 red) (4 red, 15 blue)

        maks = {RED: 0, GREEN: 0, BLUE: 0}
        for set in sets:
            # (1 red, 12 blue)
            set_cubes = set.strip().split(', ')  # (1 red) (12 blue)

            for cubes in set_cubes:
                c, t = cubes.split(' ')  # (1) (red)

                if int(c) > maks[t]:
                    # New max discovered, store it.
                    maks[t] = int(c)

        sum_power += maks[RED] * maks[GREEN] * maks[BLUE]

    print(sum_power)


if __name__ == '__main__':
    part_1(task_input)
    part_2(task_input)
