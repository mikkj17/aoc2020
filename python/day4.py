import re

from typing import List, Dict


def part1(passports: List[Dict["str", "str"]]) -> int:
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid_passports = 0
    for passport in passports:
        valid = True
        for key in required_keys:
            if key not in passport:
                valid = False
        if valid:
            valid_passports += 1
    return valid_passports


def part2(passports: List[Dict["str", "str"]]) -> int:
    required_keys = frozenset(("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))
    valid_passports = 0
    for passport in passports:

        valid = True
        for key in required_keys:
            if key not in passport:
                valid = False
        if not valid:
            continue

        if not (1920 <= int(passport["byr"]) <= 2002):
            continue
        if not (2010 <= int(passport["iyr"]) <= 2020):
            continue
        if not (2020 <= int(passport["eyr"]) <= 2030):
            continue

        match = re.match(r'^(\d+)(cm|in)$', passport['hgt'])
        if not match:
            continue
        if match[2] == 'cm' and not (150 <= int(match[1]) <= 193):
            continue
        if match[2] == 'in' and not (59 <= int(match[1]) <= 76):
            continue

        if not re.match('^#[a-f0-9]{6}$', passport["hcl"]):
            continue
        if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue
        if not re.match('^[0-9]{9}$', passport["pid"]):
            continue
        valid_passports += 1

    return valid_passports


def parse(input: str) -> List[Dict]:
    groups = input.split("\n\n")
    rv = list()
    for group in groups:
        passport = {}
        for pair in group.split():
            key, value = pair.split(":")
            passport[key] = value
        rv.append(passport)
    return rv


def main():
    filepath = "../inputs/day4.txt"
    with open(filepath) as f:
        content = f.read()
    passports = parse(content)
    print(part2(passports))


if __name__ == "__main__":
    main()
