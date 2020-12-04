#!/usr/bin/env python3
import fileinput

from passport_util import *


def is_valid(passport):
    missing = missing_fields(passport)
    return len(missing) == 0


if __name__ == "__main__":
    num_valid = num_valid_passports(passport_parser(fileinput.input()), is_valid)
    print(f"Num valid passports: {num_valid}")
