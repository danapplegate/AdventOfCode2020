#!/usr/bin/env python3
import argparse
import sys
from collections import defaultdict


def num_paths(start, end, graph):
    if start == end:
        return 1  # this final edge is one single path to the end
    sum_paths = 0
    for i, next_vertex_pair in enumerate(graph[start]):
        next_vertex, paths_from_vertex = next_vertex_pair
        if paths_from_vertex is None:
            paths_from_vertex = num_paths(next_vertex, end, graph)
        graph[start][i][1] = paths_from_vertex
        sum_paths += paths_from_vertex
    return sum_paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 9: Encoding Error")
    parser.add_argument(
        "filename", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("part", nargs="?", type=int, default=1)
    args = parser.parse_args()

    numbers = [int(n) for n in args.filename.read().split("\n") if n != ""]
    numbers.insert(0, 0)
    numbers.append(max(numbers) + 3)

    if args.part == 1:
        num_1 = num_3 = 0
        sorted_numbers = sorted(numbers)
        for i in range(0, len(sorted_numbers) - 1):
            diff = sorted_numbers[i + 1] - sorted_numbers[i]
            if diff == 1:
                num_1 += 1
            elif diff == 3:
                num_3 += 1
            else:
                print(
                    f"Invalid jump from voltage {sorted_numbers[i]} to {sorted_numbers[i+1]}"
                )
        print(num_1 * num_3)
    else:
        edges = defaultdict(list)
        max_value = max(numbers)
        for n in numbers:
            for i in range(1, 4):
                if n + i in numbers:
                    edges[n].append([n + i, None])

        print(num_paths(0, max_value, edges))
