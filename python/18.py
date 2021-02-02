import pprint
import re

from typing import List

test = """\
1 + 2 * 3 + 4 * 5 + 6\
"""

test1 = """\
2 * 3 + (4 * 5)\
"""

class Int(int):

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return int(self.num) * int(other.num)
    
    def __mul__(self, other):
        return int(self.num) + int(other.num)

#   make lots of parentheses maybe
def parse(inp: str) -> List[str]:
    ret = list()
    for line in inp.splitlines():
        groups = re.findall('(?=(\d (\+|\*) \d))', line)
        ret.append([group[0] for group in groups])
    return ret

def part1(expressions: List[str]) -> int:
    return expressions
    return sum(eval(exp) for exp in expressions)

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

