from functools import reduce
from typing import List

test = """\
abc

a
b
c

ab
ac

a
a
a
a

b"""

def compute(group: List[str]) -> int:
    return len(set("".join(group)))

def part1(groups: List[List[str]]) -> int:
    return sum([compute(group) for group in groups])
    
def compute2(group: List[str]) -> int:
    return len(reduce(lambda x, y: set(x) & set(y), group))
    
def part2(groups: List[List[str]]) -> int:
    return sum([compute2(group) for group in groups])
    

def main():
    filepath = "../inputs/06.txt"
    with open(filepath) as f:
        content = f.read()
    groups = [group.splitlines() for group in content.split("\n\n")]
    print(part2(groups))


if __name__ == "__main__":
    main()

