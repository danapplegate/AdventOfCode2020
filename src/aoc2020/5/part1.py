#!/usr/bin/env python3
import fileinput

from util import calculate_seat_id

if __name__ == "__main__":
    highest = 0
    for boarding_pass in fileinput.input():
        highest = max(highest, calculate_seat_id(boarding_pass))
    print(f"Highest seat id: {highest}")
