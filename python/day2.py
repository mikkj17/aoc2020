from typing import List


def part1(lines: List[str]):
    valid_passwords = 0
    for line in lines:
        amount, letter, password = line.split()
        lower, upper = amount.split("-")
        amount_range = range(int(lower), int(upper) + 1)
        letter = letter[0]
        if password.count(letter) in amount_range:
            valid_passwords += 1
    return valid_passwords


def part2(lines: List[str]):
    valid_passwords = 0
    for line in lines:
        positions, letter, password = line.split()
        first, second = positions.split("-")
        letter = letter[0]
        correct_positions = 0
        if password[int(first)-1] == letter:
            correct_positions += 1
        if password[int(second)-1] == letter:
            correct_positions += 1
        if correct_positions == 1:
            valid_passwords += 1
    return valid_passwords


def main():
    filepath = "../inputs/day2.txt"
    with open(filepath) as f:
        content = f.read()
    print(part2(content.split("\n")))


if __name__ == "__main__":
    main()
