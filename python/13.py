import pprint

from typing import List, Tuple

test = """\
939
7,13,x,x,59,x,31,19\
"""

test2 = """\
939
17,x,13,19\
"""

test3 = """\
939
67,7,59,61\
"""

test4 = """\
939
67,x,7,59,61\
"""

test5 = """\
939
67,7,x,59,61\
"""

test6 = """\
939
1789,37,47,1889\
"""

def parse1(inp: str) -> Tuple[int, List[int]]:
    timestamp, ids = inp.splitlines()
    return int(timestamp), [int(bus) for bus in ids.split(',') if bus != 'x']

def helper(timestamp: int, ids: List[int]) -> Tuple[int, int]:
    for bus in ids:
        if timestamp % bus == 0:
            return timestamp, bus
    return helper(timestamp+1, ids)

def part1(notes: Tuple[int, List[int]]) -> int:
    timestamp, ids = notes
    earliest, bus =  helper(timestamp, ids)
    return bus * (earliest - timestamp)


def parse2(inp: str) -> List[str]:
    return inp.splitlines()[1].split(',')

def part2(ids: List[str]) -> int:   # takes way too long. Only works for test example
    timestamp = 0
    found = False
    while not found:
        found = True
        for offset, bus in enumerate(ids):
            if bus == 'x':
                continue
            bus = int(bus)
            if timestamp < bus or (timestamp + offset) % bus != 0:
                found = False
                timestamp += 1
                break
    return timestamp

def main():
    filepath = "../inputs/13.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse2(test5)
    print(part2(parsed))

if __name__ == "__main__":
    main()

