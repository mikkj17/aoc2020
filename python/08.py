import pprint
import copy

from typing import List, Union

test = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6\
"""

class Instruction:
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = argument

    def __repr__(self):
        return f'operation: {self.operation}; argument: {self.argument}'


def parse(inp: str) -> List[Instruction]:
    return [Instruction(line.split()[0], int(line.split()[1])) for line in inp.splitlines()]

def helper(instructions: List[Instruction]) -> Union[int, bool]:
    accumulator = 0
    index = 0
    visited = set()
    done = True    # used for part 2

    while True:
        if index in visited:
            done = False
            break
        if index >= len(instructions):
            break
        instruction = instructions[index]
        visited.add(index)

        if instruction.operation == 'acc':
            index += 1
            accumulator += instruction.argument
        elif instruction.operation == 'nop':
            index += 1
        elif instruction.operation == 'jmp':
            index += instruction.argument

    return accumulator, done

def part1(instructions: List[Instruction]) -> int:
    return helper(instructions)[0]

def part2(instructions: List[Instruction]) -> int:
    for index, instruction in enumerate(instructions):
        if instruction.operation == 'jmp':
            modified = copy.deepcopy(instructions)
            modified[index].operation = 'nop'
            ret = helper(modified)
            if ret[1]:
                return ret[0]
        elif instruction.operation == 'nop':
            modified = copy.deepcopy(instructions)
            modified[index].operation = 'jmp'
            ret = helper(modified)
            if ret[1]:
                return ret[0]
    raise AssertionError('Should not come to this')

def main():
    filepath = "../inputs/08.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part2(parsed))

if __name__ == "__main__":
    main()

