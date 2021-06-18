import pprint
import re

from typing import List
from typing import Match

test = """\
1 + 2 * 3 + 4 * 5 + 6\
"""

test1 = """\
1 + (2 * 3) + (4 * (5 + 6))\
"""

test2 = """\
2 * 3 + (4 * 5)\
"""

test3 = """\
5 + (8 * 3 + 9 + 3 * 4 * 3)\
"""

test4 = """\
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))\
"""

test5 = """\
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2\
"""

paren_re = re.compile('\(([^()]*)\)')
plus_re = re.compile('(\d+) \+ (\d+)')

def paren_cb(match: Match[str]) -> str:
    return str(compute1(match[1]))

def paren_cb2(match: Match[str]) -> str:
    return str(compute2(match[1]))

def plus_cb(match: Match[str]) -> str:
    return str(int(match[1]) + int(match[2]))

def compute1(exp: str) -> int:
    parts = exp.split()
    val = int(parts[0])
    for i in range(2, len(parts), 2):
        operator = parts[i-1]
        operand = int(parts[i])
        if operator == '+':
            val += operand
        elif operator == '*':
            val *= operand
        else:
            raise AssertionError('Unknown operator:', operator)

    return val

def compute2(exp: str) -> int:
    while plus_re.search(exp):
        exp = plus_re.sub(plus_cb, exp)

    parts = exp.split()
    val = int(parts[0])
    for i in range(2, len(parts), 2):
        operator = parts[i-1]
        operand = int(parts[i])
        if operator == '+':
            val += operand
        elif operator == '*':
            val *= operand
        else:
            raise AssertionError('Unknown operator:', operator)

    return val

def evaluate1(expression: str) -> int:
    while paren_re.search(expression):
        expression = paren_re.sub(paren_cb, expression)

    return compute1(expression)

def evaluate2(expression: str) -> int:
    while paren_re.search(expression):
        expression = paren_re.sub(paren_cb2, expression)

    return compute2(expression)

def part1(expressions: List[str]) -> int:
    return sum(evaluate1(exp) for exp in expressions)

def part2(expressions: List[str]) -> int:
    return sum(evaluate2(exp) for exp in expressions)

def parse(inp: str) -> List[str]:
    return inp.splitlines()

def run_tests():
    for t in (test, test1, test2, test3, test4, test5):
        print(part2(parse(t)))

def main():
    filepath = "../inputs/18.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part2(parsed))

if __name__ == "__main__":
    main()

