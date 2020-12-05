#!/usr/bin/env python3
import fileinput

from util import calculate_seat_id

if __name__ == "__main__":
    seat_ids = []
    for boarding_pass in fileinput.input():
        seat_ids.append(calculate_seat_id(boarding_pass))
    seat_ids.sort()
    seat = seat_ids[0]
    for next_seat in seat_ids[1:]:
        seat += 1
        if seat != next_seat:
            break

    print(f"Your seat: #{seat}")
