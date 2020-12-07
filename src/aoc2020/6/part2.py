#!/usr/bin/env python3
import fileinput

if __name__ == "__main__":
    group_answers = None
    num_answers = 0

    for l in fileinput.input():
        l = l.strip()
        if l == "":
            num_answers += len(group_answers)
            group_answers = None
            continue
        if group_answers is None:
            group_answers = {c for c in l}
        else:
            group_answers &= {c for c in l}
    num_answers += len(group_answers)
    print(num_answers)
