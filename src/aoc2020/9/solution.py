#!/usr/bin/env python3
import argparse
import sys


def is_valid(numbers, target_index, preamble_size):
    preamble = numbers[target_index - preamble_size : target_index]
    target = numbers[target_index]
    complements = set()
    for n in preamble:
        if n in complements:
            return True
        complements.add(target - n)
    return False


def find_contiguous_range(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            contiguous = numbers[i : j + 1]
            contiguous_sum = sum(contiguous)
            if contiguous_sum == target:
                return contiguous


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 9: Encoding Error")
    parser.add_argument(
        "filename", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("part", nargs="?", type=int, default=1)
    parser.add_argument(
        "-s",
        dest="preamble_size",
        type=int,
        default=25,
        help="The number of previous numbers to consider (default 25)",
    )
    args = parser.parse_args()

    numbers = [int(n) for n in args.filename.read().split("\n")]

    first_invalid = None
    for i in range(args.preamble_size, len(numbers)):
        if not is_valid(numbers, i, args.preamble_size):
            first_invalid = numbers[i]
            if args.part == 1:
                print(first_invalid)
                exit
            break

    contiguous_range = find_contiguous_range(numbers, first_invalid)
    print(sum([min(contiguous_range), max(contiguous_range)]))
