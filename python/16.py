import pprint
import re
import numpy as np

from typing import List, Tuple, Dict
from collections import defaultdict
from functools import reduce

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

notes = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9\
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


def helper(rules: List[Rule], tickets: List[List[int]]) -> Tuple[int, List[List[int]]]:
    counter = 0
    valid_tickets = list()

    for ticket in tickets:
        valid_ticket = True
        for value in ticket:
            valid_value = False
            for rule in rules:
                if value in rule.ranges[0] or value in rule.ranges[1]:
                    valid_value = True
                    break
            if not valid_value:
                counter += value
                valid_ticket = False
                break
        if valid_ticket:
            valid_tickets.append(ticket)

    return counter, valid_tickets

def part1(document: Tuple[List[Rule], List[int], List[List[int]]]) -> int:
    rules, _, nearby = document
    return helper(rules, nearby)[0]

def determine_order(rules: List[Rule], tickets: List[List[int]]) -> List[Tuple[int, int]]:   # holy fuck this is ugly
    possibilities = list()

    for rule in rules:
        possible = list()
        for index in range(len(rules)):
            valid = True
            for ticket in tickets:
                value = ticket[index]
                if value not in rule.ranges[0] and value not in rule.ranges[1]:
                    valid = False
                    break
            if valid:
                possible.append(index)
        possibilities.append(possible)

    order = list()
    while len(order) < len(rules):
        for index, possible in enumerate(possibilities):
            if len(possible) == 1:
                field_index = possible[0]
                order.append((index, field_index))
                break
        for possible in possibilities:
            try:
                possible.remove(field_index)
            except:
                pass
    return order


def part2(document: Tuple[List[Rule], List[int], List[List[int]]]) -> int:  # also super ugly
    rules, ticket, nearby = document
    valid_tickets = helper(rules, nearby)[1]
    order = determine_order(rules, valid_tickets)
    departure_indices = [index for index, rule in enumerate(rules) if rule.field.startswith('departure')]
    corresponding_indices = list()
    for index in departure_indices:
        for idx, field_idx in order:
            if index == idx:
                corresponding_indices.append(field_idx)
                break

    return reduce(lambda x, y: x*y, [value for index, value in enumerate(ticket) if index in corresponding_indices])



def main():
    filepath = "../inputs/16.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part2(parsed))

if __name__ == "__main__":
    main()

