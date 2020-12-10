#!/usr/bin/env python3
import argparse
import sys


def execute_program(program):
    executed = set()
    current = accumulator = 0
    ran_successfully = False
    while current < len(program):
        if current in executed:
            break
        executed.add(current)
        line = program[current]
        command, value = line.split()
        value = int(value)
        if command == "acc":
            accumulator += value

        if command == "jmp":
            current += value
        else:
            current += 1
    if current == len(program):
        ran_successfully = True
    return ran_successfully, accumulator


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Advent of Code Day 8: Handheld Halting"
    )
    parser.add_argument(
        "filename", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("part", nargs="?", type=int, default=1)
    args = parser.parse_args()

    program = args.filename.read().split("\n")
    if program[-1] == "":
        program.pop()
    if args.part == 1:
        ran_successfully, accumulator = execute_program(program)
        print(f"Successful? {ran_successfully}, {accumulator}")
    else:
        for i, line in enumerate(program):
            new_prog = list(program)
            if line[0:3] in ["nop", "jmp"]:
                if line[0:3] == "nop":
                    new_prog[i] = f"jmp {line[3:]}"
                else:
                    new_prog[i] = f"nop {line[3:]}"
                success, accumulator = execute_program(new_prog)
                if success:
                    print(f"{accumulator}")
