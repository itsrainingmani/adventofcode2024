#!/usr/bin/env python3
from collections import *
from copy import deepcopy
from functools import cmp_to_key
from functools import cache
from itertools import *

# from util import *
import argparse
import graphlib
import math
import os
import re
import sys
import time


def print_grid(g, H, W):
    for h in range(H):
        for w in range(W):
            print(g[h, w], end="")
        print("")
    print("")


def main(test=False):
    allin = open("test.txt" if test else "input.txt").readlines()
    blocks = set()
    gloc = (0, 0)
    for y, line in enumerate(allin):
        for x, ch in enumerate(line.strip()):
            if ch == "#":
                blocks.add((y, x))
            if ch == "^":
                gloc = (y, x)

    blocks = frozenset(blocks)

    w = len(allin[0])
    h = len(allin)

    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def locs_used(blocks):
        locs = set()
        cur = gloc
        move_idx = 0
        while 0 <= cur[0] < h and 0 <= cur[1] < w:
            locs.add(cur)
            gy, gx = cur
            dy, dx = moves[move_idx % 4]
            while (gy + dy, gx + dx) in blocks:
                move_idx += 1
                dy, dx = moves[move_idx % 4]
            cur = (gy + dy, gx + dx)
        return locs

    def part1():
        return len(locs_used(blocks))

    def is_looping(blocks):
        locs = set()
        cur = gloc
        move_idx = 0
        while 0 <= cur[0] < h and 0 <= cur[1] < w:
            if (cur, move_idx) in locs:
                return True
            locs.add((cur, move_idx))
            gy, gx = cur
            dy, dx = moves[move_idx]
            while (gy + dy, gx + dx) in blocks:
                move_idx = (move_idx + 1) % 4
                dy, dx = moves[move_idx]
            cur = (gy + dy, gx + dx)
        return False

    def part2():
        options = locs_used(blocks) - frozenset([gloc])
        return sum(is_looping(blocks | frozenset([opt])) for opt in options)

    print(part1())
    print(part2())


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--test", action=argparse.BooleanOptionalAction)
    args = ap.parse_args()

    main(test=args.test)
