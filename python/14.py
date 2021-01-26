import pprint
import re

from typing import List, Tuple

test = """\
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0\
"""

test2 = """\
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1\
"""

def parse(inp: str) -> List[Tuple[str, str]]:
    ret = list()
    for line in inp.splitlines():
        assign, value = line.split(' = ')
        ret.append((assign, value))
    return ret

def mask_value(mask: str, value: str) -> str:
    ret = ''
    for index, bit in enumerate(mask):
        if bit == 'X':
            ret += value[index]
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
            memory[address] = int(mask_value(mask, bin(int(value))[2:].zfill(36)), 2)

    return sum(value for _, value in memory.items())


def mask_address(mask: str, address: str) -> str:
    ret = ''
    for index, bit in enumerate(mask):
        if bit == '0':
            ret += address[index]
        else:
            ret += bit
    return ret

def compute_addresses(address: str) -> List[str]:
    ret = list()
    count = address.count('X')
    for i in range(2**count):
        replacement = bin(i)[2:].zfill(count)
        binary = address
        for bit in replacement:
            binary = binary.replace('X', bit, 1)
        ret.append(int(binary, 2))
    return ret

def part2(program: List[Tuple[str, str]]) -> int:
    memory = dict()
    for assignment, value in program:
        if assignment == 'mask':
            mask = value
        else:
            decimal_address = re.match('mem\[(\d+)\]', assignment)[1]
            address = mask_address(mask, bin(int(decimal_address))[2:].zfill(36))
            addresses = compute_addresses(address)
            for address in addresses:
                memory[address] = int(value)

    return sum(value for _, value in memory.items())


def main():
    filepath = "../inputs/14.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part2(parsed))

if __name__ == "__main__":
    main()

