#!/usr/bin/env python3
import argparse
from time import perf_counter


def can_make(result, rest):
    if len(rest) == 1:
        return rest[0] == result

    last = rest[-1]

    if result % last == 0:
        possible_mul = can_make(result // last, rest[:-1])
    else:
        possible_mul = False

    next_power_of_10 = 1
    while next_power_of_10 <= last:
        next_power_of_10 *= 10
    if (result - last) % next_power_of_10 == 0:
        possible_concat = can_make((result - last) // next_power_of_10, rest[:-1])
    else:
        possible_concat = False

    possible_add = can_make(result - last, rest[:-1])
    return possible_mul or possible_add or possible_concat


def main(test=False):
    t1_start = perf_counter()
    ans = 0
    for line in open("test.txt" if test else "input.txt"):
        tgt, *Y = map(int, line.replace(":", "").split())
        if can_make(tgt, Y):
            ans += tgt
    t1_stop = perf_counter()

    print(ans, (t1_stop - t1_start) * 1000)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--test", action=argparse.BooleanOptionalAction)
    args = ap.parse_args()

    main(test=args.test)
