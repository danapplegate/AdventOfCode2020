#!/usr/bin/env python3
import fileinput
import re
from collections import defaultdict


def find_containers(contained, contained_by_graph, seen=set()):
    to_return = set()
    if contained not in contained_by_graph:
        return to_return
    for container in contained_by_graph.get(contained):
        to_return.add(container)
        if container not in seen:
            seen.add(container)
            to_return |= find_containers(container, contained_by_graph, seen)
    return to_return


if __name__ == "__main__":
    contained_by = defaultdict(list)
    for l in fileinput.input():
        container, contains = l.split(" bags contain ")
        matches = re.findall(r"(\d+ (\w+ \w+) bags?)+", contains)
        for _, color in matches:
            contained_by[color].append(container)

    shiny_bag_containers = find_containers("shiny gold", contained_by)
    print(shiny_bag_containers)
    print(len(shiny_bag_containers))
