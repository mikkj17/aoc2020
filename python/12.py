import pprint

from typing import List, Tuple

test = """\
F10
N3
F7
R90
F11\
"""


def parse(inp: str) -> List[Tuple[str, str]]:
    return [(ins[0], int(ins[1:])) for ins in inp.splitlines()]

def move(instructions: List[Tuple[str, str]]) -> Tuple[int, int]:
    x = y = 0
    direction = 90
    
    for action, value in instructions:
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            direction = (direction - value) % 360
        elif action == 'R':
            direction = (direction + value) % 360
        else:
            if direction == 0:
                y += value
            elif direction == 90:
                x += value
            elif direction == 180:
                y -= value
            else:
                x -= value
    return x, y

def part1(instructions: List[Tuple[str, str]]) -> int:
    x, y = move(instructions)
    return abs(x) + abs(y)

def helper(instructions: List[Tuple[str, str]]) -> Tuple[int, int]:
    waypoint_x = 10
    waypoint_y = 1
    x = y = 0

    for action, value in instructions:
        if action == 'N':
            waypoint_y += value
        elif action == 'S':
            waypoint_y -= value
        elif action == 'E':
            waypoint_x += value
        elif action == 'W':
            waypoint_x -= value
        elif action == 'L':
            if value == 90:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
            elif value == 180:
                waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
            elif value == 270:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif action == 'R':
            if value == 90:
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
            elif value == 180:
                waypoint_x, waypoint_y = -waypoint_x, -waypoint_y
            elif value == 270:
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        else:
            x += value * waypoint_x
            y += value * waypoint_y

    return x, y

def part2(instructions: List[Tuple[str, str]]) -> int:
    x, y = helper(instructions)
    return abs(x) + abs(y)


def main():
    filepath = "../inputs/12.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part2(parsed))

if __name__ == "__main__":
    main()

