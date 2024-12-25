#!/usr/bin/env python3
from collections import *
from copy import deepcopy
from functools import cmp_to_key
from itertools import *
from util import *
import argparse
import graphlib
import math
import os
import re
import sys
import time


# g, m = open('input.txt').read(), 'SAMX'

# for f, l, s in (sum, 4, (1,140,141,142)), (all, 3, (140,142)):
#     print(sum(f(g[i-x::x][:l] in (m[:l], m[:l][::-1]) for x in s)
#                 for i in range(len(g))))

data = open("input.txt").readlines()
H, W = len(data), len(data[0])-1
grid = {(y,x):data[y][x] for y in range(H) for x in range(W)}

TARGET = "XMAS"
DELTAS = [(dy,dx) for dy in [-1,0,1] for dx in [-1,0,1] if (dx != 0 or dy != 0)]
count = 0
for y, x in grid:
	for dy,dx in DELTAS:
		candidate = "".join(grid.get((y + dy*i, x + dx*i), "") for i in range(len(TARGET)))
		count += candidate == TARGET
print(count)

count = 0
for y,x in grid:
	if grid[y,x] == "A":
		lr = grid.get((y-1,x-1),"")+grid.get((y+1,x+1),"")
		rl = grid.get((y-1,x+1),"")+grid.get((y+1,x-1),"")
		count += {lr,rl} <= {"MS", "SM"}
print(count)
