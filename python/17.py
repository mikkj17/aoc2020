import pprint
import numpy as np

from typing import List

test = """\
.#.
..#
###\
"""


def parse(inp: str) -> List[List[str]]:
    return [list(line) for line in inp.splitlines()]

def compute_new_state(state: np.ndarray) -> np.ndarray:
    size = len(state)
    new_state = np.ndarray((size, size, size), dtype=str)
    print(new_state)
    for x, row in enumerate(state):
        for y, col in enumerate(row):
            for z, layer in enumerate(col):
                pass

    return new_state

def part1(initial_state: List[List[str]]) -> int:
    new_state = np.array(list(initial_state))
    new_state = new_state.reshape((*new_state.shape, 1))
    for cycle in range(6):
        new_state = compute_new_state(new_state)

def part2() -> int:
    pass

def main():
    filepath = "../inputs/17.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(test)
    print(part1(parsed))

if __name__ == "__main__":
    main()

