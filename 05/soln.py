#!/usr/bin/env python3
from collections import *
from copy import deepcopy
from functools import cmp_to_key
from itertools import *

# from util import *
import argparse
import graphlib
import math
import os
import re
import sys
import time

order = {}


# def correct_order(update):
#     topo = graphlib.TopologicalSorter()

#     for page in update:
#         topo.add(page)

#     for page in update:
#         if page in order:
#             for must_come_after in order[page]:
#                 if must_come_after in update:
#                     topo.add(page, must_come_after)
#     try:
#         return list(topo.static_order())
#     except graphlib.CycleError:
#         return None


def correct_order(me, other):
    if me not in order and other not in order:
        return me - other
    else:
        if me in order:
            if other in order[me]:
                return -1
            else:
                return 1
        elif other in order:
            if me in order[other]:
                return 1
            else:
                return -1
        return 0


def main(test=False):
    f = open("test.txt" if test else "input.txt")
    g = f.read()
    rules, updates = g.split("\n\n")
    updates = updates.split("\n")
    updates = filter(lambda x: x != "", updates)

    rules = [[int(r) for r in rule.split("|")] for rule in rules.split("\n")]
    updates = [[int(u) for u in update.split(",")] for update in updates]

    for [n, before] in rules:
        if n in order:
            order[n].add(before)
        else:
            order[n] = set([before])
    incorrects = []

    mid_sum = 0
    for update in updates:
        is_correct = True
        for i in range(0, len(update)):
            for rem in update[i + 1 :]:
                if rem in order and update[i] in order[rem]:
                    is_correct = False
                    break
            if not is_correct:
                break
        if not is_correct:
            incorrects.append(update)
        mid_sum += update[len(update) // 2] if is_correct else 0
        is_correct = True
    print("Part 1: ", mid_sum)
    mid_sum = 0
    for incor in incorrects:
        fixed = sorted(incor, key=cmp_to_key(correct_order))
        mid_sum += fixed[len(fixed) // 2]
    print("Part 2: ", mid_sum)


# test example
# 75 47 61 53 29
# 75 is before 47 61 53 29
# 47 is after 75 but before 61 53 29
# 61 is after 75 and 47 but before 53 and 29 and 13
# 53 is before 29
# 29 is last (before 13)
# 75 -> {13, 47, 29, 53, 61}
# 47 -> {29, 13, 61, 53}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-t", "--test", action=argparse.BooleanOptionalAction)
    args = ap.parse_args()

    main(test=args.test)
