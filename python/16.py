import pprint
import re

from typing import List, Tuple
from collections import namedtuple

test = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12\
"""

class Rule:

    def __init__(self, field: str, ranges: Tuple[range, range]):
        self.field = field
        self.ranges = ranges
    
    def __repr__(self):
        return f'field: {self.field}; ranges: {self.ranges}'


def parse(inp: str) -> Tuple[List[Rule], List[int], List[List[int]]]:
    rules, ticket, nearby = inp.split('\n\n')
    parsed_rules = list()
    for rule in rules.splitlines():
        matches = re.match('(.*): (\d+)-(\d+) or (\d+)-(\d+)', rule)
        field, first_lower, first_upper, second_lower, second_upper = matches.groups()
        ranges = (range(int(first_lower), int(first_upper) + 1), range(int(second_lower), int(second_upper) + 1))
        parsed_rules.append(Rule(field, ranges))

    your_ticket = [int(value) for value in ticket.splitlines()[1].split(',')]
    nearby_tickets = list()
    for ticket in nearby.splitlines()[1:]:
        nearby_tickets.append([int(value) for value in ticket.split(',')])

    return parsed_rules, your_ticket, nearby_tickets

def part1(document: Tuple[List[Rule], List[int], List[List[int]]]) -> int:
    rules, ticket, nearby = document
    counter = 0

    for ticket in nearby:
        for value in ticket:
            valid = False
            for rule in rules:
                if value in rule.ranges[0] or value in rule.ranges[1]:
                    valid = True
                    break
            if not valid:
                counter += value

    return counter

def part2() -> int:
    pass

def main():
    filepath = "../inputs/16.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part1(parsed))

if __name__ == "__main__":
    main()

