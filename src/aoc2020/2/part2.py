#!/usr/bin/env python3
import fileinput

if __name__ == "__main__":
    num_valid = 0
    for line in fileinput.input():
        policy, password = line.split(":")
        password = password.strip()
        char_count, char = policy.split(" ")
        pos1, pos2 = char_count.split("-")
        pos1 = int(pos1) - 1
        pos2 = int(pos2) - 1
        char1 = password[pos1]
        char2 = password[pos2]
        if (char1 == char or char2 == char) and char1 != char2:
            num_valid += 1
    print(f"Num valid passwords: {num_valid}")
