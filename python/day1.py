from typing import List


def part1(numbers: List[int]):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            first_number = numbers[i]
            second_number = numbers[j]
            if first_number + second_number == 2020:
                return first_number * second_number
    return 0


def part2(numbers: List[int]):
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)):
                first_number = numbers[i]
                second_number = numbers[j]
                third_number = numbers[k]
                if first_number + second_number + third_number == 2020:
                    return first_number * second_number * third_number
    return 0


def main():
    filepath = "../inputs/day1.txt"
    with open(filepath) as f:
        content = f.read()
    print(part2([int(x) for x in content.split()]))


if __name__ == "__main__":
    main()

