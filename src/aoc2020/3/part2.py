#!/usr/bin/env python3
import fileinput

from forest_map import ForestMap

if __name__ == "__main__":
    lines = fileinput.input()
    fm = ForestMap(lines)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for right, down in slopes:
        product *= fm.num_trees(right, down)
    print(f"Product of all trees: {product}")
