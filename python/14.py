import pprint
import re

from typing import List, Tuple

test = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0\
"""


def parse(inp: str) -> List[Tuple[str, str]]:
    ret = list()
    for line in inp.splitlines():
        assign, value = line.split(' = ')
        ret.append((assign, value))
    return ret

def mask_bits(mask: str, bits: str) -> str:
    ret = ''
    for index, bit in enumerate(mask):
        if bit == 'X':
            ret += bits[index]
        else:
            ret += bit
    return ret

def part1(program: List[Tuple[str, str]]) -> int:
    memory = dict()
    for assignment, value in program:
        if assignment == 'mask':
            mask = value
        else:
            address = re.match('mem\[(\d+)\]', assignment)[1]
            memory[address] = int(mask_bits(mask, bin(int(value))[2:].zfill(36)), 2)

    return sum(value for _, value in memory.items())

def part2() -> int:
    pass

def main():
    filepath = "../inputs/14.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part1(parsed))

if __name__ == "__main__":
    main()

