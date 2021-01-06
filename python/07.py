import pprint

from typing import List, Dict

test = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.\
"""

test2 = """\
shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.\
"""

class Bag:
    def __init__(self, description, amount):
        self.description = description
        self.amount = int(amount)

    def __repr__(self):
        return f'{self.amount}: {self.description}'


class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = set_bags(right)

    def __repr__(self):
        return f'{self.left} => {self.right}'


def set_bags(right_side: str) -> List[Bag]:
    bags = list()
    for rule in right_side.split(', '):
        if rule[0] == 'n':
            bags.append(Bag('no other bags', 0))
        else:
            bags.append(Bag(" ".join(rule.split()[1:3]), rule[0]))
    return bags


def parse(inp: str) -> Dict[str, List[Bag]]:
    rules = list()
    for line in inp.splitlines():
        left, right = line.split(' bags contain ')
        rules.append(Rule(left, right))
    return {rule.left: rule.right for rule in rules}


def compute(left: str, mapping: Dict[str, List[Bag]]) -> bool:
    right = mapping[left]
    descriptions = [r.description for r in right]
    if 'shiny gold' in descriptions:
        return True
    if 'no other bags' in descriptions:
        return False
    return True in [compute(r.description, mapping) for r in right]


def part1(rules: Dict[str, List[Bag]]) -> int:
    return [compute(rule, rules) for rule in rules].count(True)


def compute2(left: str, mapping: Dict[str, List[Bag]]) -> int:
    right = mapping[left]
    descriptions = [r.description for r in right]
    if 'no other bags' in descriptions:
        return 0
    return sum([r.amount + r.amount * compute2(r.description, mapping) for r in right])
    

def part2(rules: Dict[str, List[Bag]]) -> int:
    return compute2('shiny gold', rules)


def main():
    filepath = "../inputs/07.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part2(parsed))

if __name__ == "__main__":
    main()

