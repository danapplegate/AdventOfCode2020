#!/usr/bin/env python3
import fileinput

if __name__ == "__main__":
    # Loop through all lines, checking to see if we've
    # seen the complement of this number and 2020 (already in
    # the set). If not, calculate the complement and add it
    complements = set()
    for line in fileinput.input():
        num = int(line)
        orig_num = 2020 - num
        if num in complements:
            print(f"{num} * {orig_num} = {num * orig_num}")
            break
        complements.add(orig_num)
