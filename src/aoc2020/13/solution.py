#!/usr/bin/env python3
import argparse
import math
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Advent of Code Day 13: Shuttle Search"
    )
    parser.add_argument(
        "filename", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("part", nargs="?", type=int, default=1)
    args = parser.parse_args()

    lines = args.filename.read().split("\n")

    if args.part == 1:
        arrival = int(lines[0])
        earliest = arrival
        buses = [int(n) for n in lines[1].split(",") if n != "x"]
        found = False
        while not found:
            earliest += 1
            for bus in buses:
                if earliest % bus == 0:
                    found = True
                    break
        print((earliest - arrival) * bus)
    else:
        raw_buses = lines[1].split(",")
        buses = list()
        for b in raw_buses:
            if not b == "x":
                b = int(b)
            buses.append(b)
        t = 0
        increment = buses[0]
        for i, bus in enumerate(buses):
            if bus == "x":
                continue
            remainder = (t + i) % bus
            while remainder != 0:
                t += increment
                remainder = (t + i) % bus
            increment = math.lcm(*[n for n in buses[: i + 1] if isinstance(n, int)])
        print(t)
