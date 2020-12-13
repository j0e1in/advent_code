import re

with open("input/day4.txt") as f:
    passports = f.read().strip().split("\n\n")
    passports = [" ".join(p.split("\n")).strip().split(" ") for p in passports]

fields_to_validate = set(
    [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
        # "cid",
    ]
)

rules = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193)
                  or (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: re.match("#[a-f0-9]{6}", x) is not None,
    "ecl": lambda x: x in set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]),
    "pid": lambda x: re.match("[0-9]{9}", x) is not None,
    "cid": lambda x: True,
}


def fields_valid(passport):
    for f in passport:
        field, data = f.split(":")
        if not rules[field](data):
            print(f)
            return False
    return True


def part1(fields):
    len(fields_to_validate.difference(fields)) == 0


def part2(fields):
    len(fields_to_validate.difference(fields)) == 0 and fields_valid(p)


valid_passports_part1 = 0
valid_passports_part2 = 0

for p in passports:
    fields = set([f.split(":")[0] for f in p])
    valid_passports_part1 += 1 if part1(fields) else 0
    valid_passports_part1 += 1 if part2(fields) else 0

print(valid_passports_part1)
print(valid_passports_part2 - 1)
