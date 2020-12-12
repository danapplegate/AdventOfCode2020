#!/usr/bin/env python3
import argparse
import copy
import sys
from math import atan, cos, degrees, radians, sin


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattan_distance_to(self, target):
        return abs(target.x - self.x) + abs(target.y - self.y)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate(self, degrees):
        degrees %= 360
        if degrees == 90:
            self.x, self.y = -self.y, self.x
        elif degrees == 180:
            self.x, self.y = -self.x, -self.y
        elif degrees == 270:
            self.x, self.y = self.y, -self.x


class Ferry:
    def __init__(self, position=(0, 0), orientation=0, version=1):
        if not isinstance(position, Coordinate):
            x, y = position
            position = Coordinate(x, y)
        self.original_position = copy.copy(position)
        self.position = position
        self.orientation = orientation
        self.waypoint = Vector(10, 1)
        self._version = version

    def execute_command(self, raw_command):
        command = raw_command[0]
        value = int(raw_command[1:])
        if self._version == 1:
            self.command_v1(command, value)
        else:
            self.command_v2(command, value)

    def command_v1(self, command, value):
        if command in ["R", "L"]:
            if command == "R":
                value = -value
            self.orientation += value
            self.orientation %= 360
        elif command == "F":
            if self.orientation in [180, 270]:
                value = -value
            if self.orientation in [90, 270]:
                self.position.y += value
            else:
                self.position.x += value
        else:
            if command in ["W", "S"]:
                value = -value
            if command in ["W", "E"]:
                self.position.x += value
            else:
                self.position.y += value

    def command_v2(self, command, value):
        if command in ["R", "L"]:
            if command == "R":
                value = -value
            self.waypoint.rotate(value)
        elif command == "F":
            self.position.x += value * self.waypoint.x
            self.position.y += value * self.waypoint.y
        else:
            if command in ["W", "S"]:
                value = -value
            if command in ["W", "E"]:
                self.waypoint.x += value
            else:
                self.waypoint.y += value

    def manhattan_distance_traveled(self):
        return self.original_position.manhattan_distance_to(self.position)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 12: Rain Risk")
    parser.add_argument(
        "filename", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("part", nargs="?", type=int, default=1)
    args = parser.parse_args()

    ferry = Ferry(version=args.part)
    for line in args.filename.read().split("\n"):
        ferry.execute_command(line)
    print(ferry.manhattan_distance_traveled())
