from pprint import pprint
from typing import List
from copy import deepcopy

test = """\
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL\
"""

empty = 'L'
occupied = '#'

def parse(inp: str) -> List[str]:
    return [[seat for seat in row] for row in inp.splitlines()]

def adjacent_occupied(seats: List[str], row: int, col: int) -> int:
    occupied_counter = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(seats) and 0 <= j < len(seats[0]):
                if i != row or j != col:
                    neighbour = seats[i][j]
                    if neighbour == occupied:
                        occupied_counter += 1
    return occupied_counter

def compute_new_state(seats: List[str]) -> List[str]:
    new_state = deepcopy(seats)
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            seat = seats[row][col]
            amount_occupied = adjacent_occupied(seats, row, col)
            if seat == empty:
                if amount_occupied == 0:
                    new_state[row][col] = occupied
            elif seat == occupied:
                if amount_occupied >= 4:
                    new_state[row][col] = empty

    return new_state


def part1(seats: List[str]) -> int:
    old_state = deepcopy(seats)
    new_state = deepcopy(seats)
    while True:
        new_state = compute_new_state(old_state)
        if new_state == old_state:
            break
        old_state = deepcopy(new_state)
    
    return sum([row.count(occupied) for row in new_state])

def part2() -> int:
    pass

def main():
    filepath = "../inputs/11.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part1(parsed))

if __name__ == "__main__":
    main()

