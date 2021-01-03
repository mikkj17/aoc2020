from typing import List, Tuple


def seat_id(boarding_pass: str) -> int:
    row = int("".join(['0' if char == 'F' else '1' for char in boarding_pass[:7]]), 2)
    col = int("".join(['0' if char == 'L' else '1' for char in boarding_pass[7:]]), 2)
    return row * 8 + col
    

def part1(passes: List[str]) -> int:
    return max([seat_id(boarding_pass) for boarding_pass in passes])
    
    
def part2(passes: List[str]) -> int:
    seats = sorted([seat_id(boarding_pass) for boarding_pass in passes])
    for index, seat in enumerate(seats[:-1]):
        next = seats[index+1]
        if next - seat > 1:
            return seat+1
    return -1



def main():
    filepath = "../inputs/05.txt"
    with open(filepath) as f:
        content = f.read()
    print(part2(content.splitlines()))


if __name__ == "__main__":
    main()

