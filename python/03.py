import math

from typing import List


def part1(hill: List[str]):
    trees_encountered = 0
    toboggan = True
    x, y = (0, 0)
    while toboggan:
        if hill[x][y] == "#":
            trees_encountered += 1
        x += 1
        y = (y + 3) % len(hill[0])
        if len(hill) <= x:
            toboggan = False
    return trees_encountered


def part2_helper(hill: List[str], right: int, down: int):
    trees_encountered = 0
    toboggan = True
    x, y = (0, 0)
    while toboggan:
        if hill[x][y] == "#":
            trees_encountered += 1
        x += down
        y = (y + right) % len(hill[0])
        if len(hill) <= x:
            toboggan = False
    return trees_encountered


def part2(hill: List[str]):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    return math.prod([part2_helper(hill, right, down) for right, down in slopes])


def main():
    filepath = "../inputs/03.txt"
    with open(filepath) as f:
        content = f.read()
    print(part2(content.split("\n")))


if __name__ == "__main__":
    main()

