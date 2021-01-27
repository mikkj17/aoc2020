import pprint

from typing import List
from collections import defaultdict

test = """\
0,3,6\
"""


def parse(inp: str) -> List[int]:
    return [int(num) for num in inp.split(',')]

def part1(nums: List[int]) -> int:
    spoken = list()
    for turn in range(2020):
        if turn < len(nums):
            new = nums[turn]
        else:
            prev = spoken[-1]
            if prev in spoken[:-1]:
                new = (turn-1) - max(index for index, num in enumerate(spoken[:-1]) if num == prev)
            else:
                new = 0
        spoken.append(new)
    return spoken[-1]

def part2(nums: List[int]) -> int:
    spoken = list()
    seen = defaultdict(list)
    for turn in range(30000000):
        if turn < len(nums):
            new = nums[turn]
            seen[new].append(turn)
        else:
            prev = spoken[-1]
            if len(seen[prev]) > 1:
                prev_index, last_index = seen[prev][-2:]
                new = last_index - prev_index
                seen[new].append(turn)
            else:
                new = 0
                seen[new].append(turn)
        spoken.append(new)
    return new


def main():
    filepath = "../inputs/15.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part2(parsed))

if __name__ == "__main__":
    main()

