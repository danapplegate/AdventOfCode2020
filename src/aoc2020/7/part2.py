#!/usr/bin/env python3
import fileinput
import re
from collections import defaultdict


def count_contents(container, contains_bags_graph):
    if container not in contains_bags_graph:
        return 0
    return sum(
        [
            n + n * count_contents(bag_type, contains_bags_graph)
            for n, bag_type in contains_bags_graph[container]
        ]
    )


if __name__ == "__main__":
    contains_bags = defaultdict(list)
    for l in fileinput.input():
        container, contains = l.split(" bags contain ")
        matches = re.findall(r"(\d+) (\w+ \w+) bags?", contains)
        contains_bags[container].extend([(int(n), bag_type) for n, bag_type in matches])
    print(count_contents("shiny gold", contains_bags))
