from collections import deque
from itertools import pairwise
from operator import mul
import re


instrs = []
with open("input.txt") as file:
    for line in file:
        instrs.append(line)
instrs = "".join(instrs)


def calc_mul(input):
    return sum(
        [
            mul(int(x.group(1)), int(x.group(2)))
            for x in re.finditer(r"mul\((\d+)\,(\d+)\)", input)
        ]
    )


mul_sum = 0

dodont = deque([x for x in re.finditer(r"do\(\)|don\'t\(\)", instrs)])
while dodont:
    if instrs[dodont[0].start() : dodont[0].end()] == "do()":
        break
    else:
        dodont.popleft()
# basically all muls till the first do() are enabled
mul_sum += calc_mul(instrs[0 : dodont[0].start()])
was_do = True
start_pos = dodont[0].end()
end_pos = len(instrs) - 1

for d1, d2 in pairwise(dodont):
    match (d1.group(0), d2.group(0)):
        case (x, y) if x == y:
            continue
        case ("do()", "don't()"):
            end_pos = d2.start()
            was_do = False
        case ("don't()", "do()"):
            was_do = True
            start_pos = d2.end()
    mul_sum += calc_mul(instrs[start_pos:end_pos])

if was_do:
    # we ended on a do()
    mul_sum += calc_mul(instrs[start_pos : len(instrs) - 1])

print(mul_sum)
