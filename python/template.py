import pprint

from typing import List

test = """\
\
"""


def parse(inp: str) -> None:
    pass

def part1() -> int:
    pass

def part2() -> int:
    pass

def main():
    filepath = "../inputs/01.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(test)
    print(part1(parsed))

if __name__ == "__main__":
    main()

