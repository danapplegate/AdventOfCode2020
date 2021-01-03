#!/usr/bin/env python3
import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Advent of Code Day 15: Rambunctious Recitation"
    )
    parser.add_argument(
        "filename", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("part", nargs="?", type=int, default=1)
    args = parser.parse_args()

    lines = args.filename.read().split("\n")

    if args.part == 1:
        end_turn = 2020
    else:
        end_turn = 30000000
    for l in lines:
        numbers = [int(n) for n in l.split(",")]
        spoken = {int(n): i for i, n in enumerate(numbers[:-1], 1)}
        turn = len(numbers) + 1
        while turn <= end_turn:
            last_spoken = numbers[-1]
            if last_spoken not in spoken:
                numbers.append(0)
            else:
                numbers.append(turn - 1 - spoken[last_spoken])
            spoken[last_spoken] = turn - 1
            turn += 1
        print(numbers[-1])
