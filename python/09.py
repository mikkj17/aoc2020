import pprint

from typing import List

test = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576\
"""

def parse(inp: str) -> List[int]:
    return [int(x) for x in inp.splitlines()]


def valid(number: int, numbers: List[int]) -> bool:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if numbers[i] + numbers[j] == number:
                return True
    return False

def part1(numbers: List[int], preamble_length: int) -> int:
    for index, number in enumerate(numbers[preamble_length:], start=preamble_length):
        if not valid(number, numbers[index-preamble_length:index]):
            return number
    raise AssertionError("Should not come to this")


def part2(numbers: List[int]) -> int:
    pass


def main():
    filepath = "../inputs/09.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part1(parsed, 25))

if __name__ == "__main__":
    main()

