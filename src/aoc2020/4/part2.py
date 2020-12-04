#!/usr/bin/env python3
import fileinput
import re

from passport_util import *


def year_range_validator(min, max):
    def validator(year_string):
        if len(year_string) != 4:
            return False
        year = int(year_string)
        return min <= year and year <= max

    return validator


def hgt_validator(hgt):
    match = re.fullmatch(r"(\d+)(in|cm)", hgt)
    if not match:
        return False
    height = int(match[1])
    if match[2] == "cm":
        return 150 <= height and height <= 193
    else:
        return 59 <= height and height <= 76


validators = {
    "byr": year_range_validator(1920, 2002),
    "iyr": year_range_validator(2010, 2020),
    "eyr": year_range_validator(2020, 2030),
    "hgt": hgt_validator,
    "hcl": lambda hcl: bool(re.fullmatch(r"#[0-9A-Fa-f]{6}", hcl)),
    "ecl": lambda ecl: ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda pid: bool(re.fullmatch(r"\d{9}", pid)),
    "cid": lambda _: True,
}


def is_valid(passport):
    global validators
    missing = missing_fields(passport)
    if len(missing) > 0:
        return False
    return all([validators[key](value) for key, value in passport.items()])


if __name__ == "__main__":
    num_valid = num_valid_passports(passport_parser(fileinput.input()), is_valid)
    print(f"Num valid: {num_valid}")
