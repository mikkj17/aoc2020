from pprint import pprint
from typing import List, Generator, Tuple
from itertools import combinations

small = """\
16
10
15
5
1
11
7
19
6
12
4\
"""

test = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3\
"""

def parse(inp: str) -> List[int]:
    sorted_list = sorted([int(x) for x in inp.splitlines()])
    return sorted_list + [sorted_list[-1] + 3]

def compute_differences(numbers: List[int]) -> Tuple[int, int]:
    differences = list()
    n = 0
    for num in numbers:
        differences.append(num-n)
        n = num
    return differences.count(1), differences.count(3)


def part1(numbers: List[int]) -> int:
    differences = compute_differences(numbers)
    return differences[0] * differences[1]

def compute_arrangements(numbers: List[int], minimum_length: int) -> List[Generator[int, None, None]]:
    return [combinations(numbers, length) for length in range(minimum_length, len(numbers) + 1)]


def valid_arrangement(numbers: List[int], jolt_adaptor: int) -> bool:
    if numbers[-1] != jolt_adaptor:
        return False
    n = 0
    for num in numbers:
        if num-n > 3:
            return False
        n = num
    return True

def part2(numbers: List[int]) -> int:
    return numbers

def main():
    filepath = "../inputs/10.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(test)
    print(part2(parsed))

if __name__ == "__main__":
    main()

