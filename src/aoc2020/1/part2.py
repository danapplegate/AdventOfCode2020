#!/usr/bin/env python3
import fileinput

if __name__ == "__main__":
    # Similar to part one, we need to loop over all
    # the number pairs, calculate the complement, then scan
    # through the remainder of the list for that complement
    nums = [int(n) for n in fileinput.input()]
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums[i + 1 :]):
            target = 2020 - num1 - num2
            if target in nums[j + 1 :]:
                print(f"{num1} * {num2} * {target} = {num1 * num2 * target}")
                break
