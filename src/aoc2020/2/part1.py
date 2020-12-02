#!/usr/bin/env python3
import fileinput

if __name__ == "__main__":
    num_valid = 0
    for line in fileinput.input():
        policy, password = line.split(":")
        char_count, char = policy.split(" ")
        low, high = char_count.split("-")
        low = int(low)
        high = int(high)
        char_count = 0
        for c in password:
            if c == char:
                char_count += 1
        if low <= char_count and char_count <= high:
            num_valid += 1
    print(f"Num valid passwords: {num_valid}")
