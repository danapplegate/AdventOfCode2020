#!/usr/bin/env python3
import fileinput

from forest_map import ForestMap

if __name__ == "__main__":
    lines = fileinput.input()
    fm = ForestMap(lines)
    print(f"Num trees: {fm.num_trees(3, 1)}")
