#!/usr/bin/env python3
import fileinput

if __name__ == "__main__":
    group_answers = set()
    sum_answers = 0
    for line in fileinput.input():
        line = line.strip()
        if line == "":
            sum_answers += len(group_answers)
            group_answers = set()
        group_answers |= {c for c in line}
    # Remember to process last group
    sum_answers += len(group_answers)
    print(sum_answers)
