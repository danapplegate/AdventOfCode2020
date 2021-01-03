#!/usr/bin/env python3
import argparse
import sys


def expand_addresses(addr: str):
    if "X" in addr:
        addr = list(addr)
        expanded = list()
        i = addr.index("X")
        addr[i] = "0"
        e = expand_addresses("".join(addr))
        if isinstance(e, str):
            expanded.append(e)
        else:
            expanded.extend(e)
        addr[i] = "1"
        e = expand_addresses("".join(addr))
        if isinstance(e, str):
            expanded.append(e)
        else:
            expanded.extend(e)
        return expanded
    else:
        return addr


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of Code Day 14: Docking Data")
    parser.add_argument(
        "filename", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    parser.add_argument("part", nargs="?", type=int, default=1)
    args = parser.parse_args()

    lines = args.filename.read().split("\n")

    mem = dict()
    mask = ""
    for l in lines:
        if "mask" == l[:4]:
            mask = l[7:]
        else:
            assignment, val = l.split(" = ")
            address = int(assignment[4:-1])
            val = int(val)
            if args.part == 1:
                bin = format(val, "0>36b")
                result = list()
                for m, b in zip(mask, bin):
                    if m != "X":
                        result.append(m)
                    else:
                        result.append(b)
                result_val = "".join(result)
                mem[address] = int(result_val, 2)
            else:
                address = format(address, "0>36b")
                new_addr = list()
                for m, a in zip(mask, address):
                    if m == "0":
                        new_addr.append(a)
                    else:
                        new_addr.append(m)
                new_addr = "".join(new_addr)
                all_addr = expand_addresses(new_addr)
                for a in all_addr:
                    mem[int(a, 2)] = val

    print(sum(mem.values()))
