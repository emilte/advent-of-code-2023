"""
https://adventofcode.com/2023/day/5
"""
from utils import timeit
from task_input2 import task_input, sample


def extract_lines(cmap):
    lines = cmap.split(':')[1].strip().split('\n')
    return [[int(n) for n in l.split()] for l in lines]


@timeit
def part_1(task_input) -> None:
    """Solution to part 1."""
    maps = task_input.strip().split('\n\n')
    seeds = [int(s) for s in maps[0].split(': ')[1].split()]

    seed_map = {seed: [seed] for seed in seeds}
    for seed in seeds:
        for raw_category_map in maps[1:]:
            lines = extract_lines(raw_category_map)
            added = False

            for dst, src, r in lines:
                current = seed_map[seed][-1]
                if current in range(src, src + r):
                    seed_map[seed].append(dst + current - src)
                    added = True
                    break

            if not added:
                seed_map[seed].append(current)

    print(min([m[-1] for m in seed_map.values()]))


@timeit
def part_2(task_input) -> None:
    """Solution to part 2."""
    maps = task_input.strip().split('\n\n')
    seedss = [int(s) for s in maps[0].split(': ')[1].split()]
    seeds = []
    for i in range(0, len(seedss), 2):
        s = seedss[i]
        r = s + seedss[i + 1]
        seeds.extend(list(range(s, r)))

    print()

    # seed_map = {seed: [seed] for seed in seeds}
    # for seed in seeds:
    #     for raw_category_map in maps[1:]:
    #         lines = extract_lines(raw_category_map)
    #         added = False

    #         for dst, src, r in lines:
    #             current = seed_map[seed][-1]
    #             if current in range(src, src + r):
    #                 seed_map[seed].append(dst + current - src)
    #                 added = True
    #                 break

    #         if not added:
    #             seed_map[seed].append(current)

    # print(min([m[-1] for m in seed_map.values()]))


if __name__ == '__main__':
    # part_1(sample)
    # part_1(task_input)
    # part_2(sample)
    part_2(task_input)
