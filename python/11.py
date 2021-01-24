from pprint import pprint
from typing import List, Tuple
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

def parse(inp: str) -> List[List[str]]:
    return [[seat for seat in row] for row in inp.splitlines()]

def adjacent_occupied(seats: List[List[str]], row: int, col: int) -> int:
    occupied_counter = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < len(seats) and 0 <= j < len(seats[0]):
                if i != row or j != col:
                    neighbour = seats[i][j]
                    if neighbour == occupied:
                        occupied_counter += 1
    return occupied_counter

def compute_new_state(seats: List[List[str]]) -> List[List[str]]:
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


def part1(seats: List[List[str]]) -> int:
    old_state = deepcopy(seats)
    new_state = deepcopy(seats)
    while True:
        new_state = compute_new_state(old_state)
        if new_state == old_state:
            break
        old_state = deepcopy(new_state)
    
    return sum([row.count(occupied) for row in new_state])


def find_neighbour(seats: List[List[List[str]]], row: int, col: int, direction: str) -> bool:
    while True:

        if direction == 'up':
            if row > 0:
                row -= 1
            else:
                return False
        elif direction == 'down':
            if row < len(seats)-1:
                row += 1
            else:
                return False
        elif direction == 'left':
            if col > 0:
                col -= 1
            else:
                return False
        elif direction == 'right':
            if col < len(seats[0])-1:
                col += 1
            else:
                return False

        if direction == 'up-left':
            if row > 0 and col > 0:
                row -= 1
                col -= 1
            else:
                return False
        elif direction == 'down-left':
            if row < len(seats)-1 and col > 0:
                row += 1
                col -= 1
            else:
                return False
        elif direction == 'up-right':
            if row > 0 and col < len(seats[0])-1:
                row -= 1
                col += 1
            else:
                return False
        elif direction == 'down-right':
            if row < len(seats)-1 and col < len(seats[0])-1:
                row += 1
                col += 1
            else:
                return False


        seat = seats[row][col]
        if seat == occupied:
            return True
        elif seat == empty:
            return False
    

def get_new_state(seats: List[List[str]]) -> List[List[str]]:
    new_state = deepcopy(seats)
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            seat = seats[row][col]
            amount_occupied = [
                find_neighbour(seats, row, col, dir) 
                for dir in ['up', 'down', 'left', 'right', 'up-left', 'down-left', 'up-right', 'down-right']
            ].count(True)
            if seat == empty:
                if amount_occupied == 0:
                    new_state[row][col] = occupied
            elif seat == occupied:
                if amount_occupied >= 5:
                    new_state[row][col] = empty

    return new_state



def part2(seats: List[List[str]]) -> int:
    old_state = deepcopy(seats)
    new_state = deepcopy(seats)
    while True:
        new_state = get_new_state(old_state)
        if new_state == old_state:
            break
        old_state = deepcopy(new_state)
    
    return sum([row.count(occupied) for row in new_state])


def main():
    filepath = "../inputs/11.txt"
    with open(filepath) as f:
        content = f.read()
    parsed = parse(content)
    print(part2(parsed))

if __name__ == "__main__":
    main()

