#!/usr/bin/env python3
import argparse
import sys
from copy import deepcopy


def is_empty_seat(character):
    return character == "L"


def is_occupied_seat(character):
    return character == "#"


def in_bounds(seat_map, row, column):
    return (
        0 <= row and row < len(seat_map) and 0 <= column and column < len(seat_map[0])
    )


def no_adjacent_occupied_seats(seat_map, row, column):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            check_r = row + i
            check_c = column + j
            if in_bounds(seat_map, check_r, check_c) and is_occupied_seat(
                seat_map[check_r][check_c]
            ):
                return False
    return True


def four_adjacent_occupied_seats(seat_map, row, column):
    num_occupied = -1  # start at -1 to offset the occupied seat we're checking
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            check_r = row + i
            check_c = column + j
            if in_bounds(seat_map, check_r, check_c) and is_occupied_seat(
                seat_map[check_r][check_c]
            ):
                num_occupied += 1
            if num_occupied >= 4:
                return True
    return False


def is_occupied_visible(seat_map, start, delta):
    dr, dc = delta
    if dr == 0 and dc == 0:
        return False
    r, c = start
    check_r = r + dr
    check_c = c + dc
    while (
        0 <= check_r
        and check_r < len(seat_map)
        and 0 <= check_c
        and check_c < len(seat_map[0])
    ):
        char = seat_map[check_r][check_c]
        if is_occupied_seat(char):
            return True
        elif is_empty_seat(char):
            return False
        check_r += dr
        check_c += dc
    return False


def count_occupied_visible(seat_map, row, column):
    num_occupied_visible = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if is_occupied_visible(seat_map, (row, column), (i, j)):
                num_occupied_visible += 1
    return num_occupied_visible


def count_occupied(seat_map):
    return sum([1 for row in seat_map for char in row if is_occupied_seat(char)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Advent of Code Day 11: Seating System"
    )
    parser.add_argument(
        "filename", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("part", nargs="?", type=int, default=1)
    args = parser.parse_args()

    raw_content = args.filename.read().split("\n")
    seat_map = [list(line) for line in raw_content]

    changed = True
    while changed:
        new_seat_map = deepcopy(seat_map)
        for i, row in enumerate(seat_map):
            for j, column in enumerate(row):
                if args.part == 1:
                    if is_empty_seat(column) and no_adjacent_occupied_seats(
                        seat_map, i, j
                    ):
                        new_seat_map[i][j] = "#"
                    elif is_occupied_seat(column) and four_adjacent_occupied_seats(
                        seat_map, i, j
                    ):
                        new_seat_map[i][j] = "L"
                else:
                    num_occupied_visible = count_occupied_visible(seat_map, i, j)
                    if is_empty_seat(column) and num_occupied_visible == 0:
                        new_seat_map[i][j] = "#"
                    elif is_occupied_seat(column) and num_occupied_visible >= 5:
                        new_seat_map[i][j] = "L"
        changed = new_seat_map != seat_map
        seat_map = new_seat_map
    print("\n".join(["".join(r) for r in seat_map]))
    print(count_occupied(seat_map))
