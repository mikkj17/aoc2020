import collections
import pprint

from typing import List, Set, Tuple

test = """\
.#.
..#
###\
"""


def parse(inp: str) -> Set[Tuple[int, int, int]]:
    ret = set()
    for x, line in enumerate(inp.splitlines()):
        for y, char in enumerate(line):
            if char == '#':
                ret.add((x, y, 0))
    return ret


def part1(activated: Set[Tuple[int, int, int]]) -> int:
    for _ in range(6):
        marked = collections.Counter()
        for x, y, z in activated:
            for x_i in (-1, 0, 1):
                for y_i in (-1, 0, 1):
                    for z_i in (-1, 0, 1):
                        if x_i == y_i == z_i == 0:
                            continue
                        marked[(x + x_i, y + y_i, z + z_i)] += 1

        new_activated = set()
        for cube in activated:
            if marked[cube] in {2, 3}:
                new_activated.add(cube)

        for cube, counter in marked.items():
            if counter == 3:
                new_activated.add(cube)
                activated = new_activated

    return len(activated)


def parse2(inp: str) -> Set[Tuple[int, int, int, int]]:
    ret = set()
    for x, line in enumerate(inp.splitlines()):
        for y, char in enumerate(line):
            if char == '#':
                ret.add((x, y, 0, 0))
    return ret


def part2(activated: Set[Tuple[int, int, int, int]]) -> int:
    for _ in range(6):
        marked = collections.Counter()
        for x, y, z, w in activated:
            for x_i in (-1, 0, 1):
                for y_i in (-1, 0, 1):
                    for z_i in (-1, 0, 1):
                        for w_i in (-1, 0, 1):
                            if x_i == y_i == z_i == w_i == 0:
                                continue
                            marked[(x + x_i, y + y_i, z + z_i, w + w_i)] += 1

        new_activated = set()
        for cube in activated:
            if marked[cube] in {2, 3}:
                new_activated.add(cube)

        for cube, counter in marked.items():
            if counter == 3:
                new_activated.add(cube)
                activated = new_activated

    return len(activated)



def main():
    filepath = "../inputs/17.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse2(content)
    print(part2(parsed))


if __name__ == "__main__":
    main()

