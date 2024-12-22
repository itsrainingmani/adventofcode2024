from itertools import pairwise
from pprint import pprint


inputs = []
with open("input.txt") as file:
    for line in file:
        inputs.append(list(map(int, line.strip().split(" "))))


def is_safe(report):
    # given a report with a level removed, check if it's safe
    diffs = [b - a for a, b in pairwise(report)]
    is_safe = True
    # num_unsafes = 0
    for d1, d2 in pairwise(diffs):
        if (
            (abs(d1) < 1 or abs(d1) > 3)
            or (abs(d2) < 1 or abs(d2) > 3)
            or (d1 * d2 < 0)
        ):
            is_safe = False
            break
    return is_safe


def solution():
    # part 1 is checking how many reports are safe
    # part 2 is probably checking how unsafe a report is
    safe1, safe2 = 0, 0
    for report in inputs:
        safe1 += 1 if is_safe(report) else 0
        for i in range(len(report)):
            l = report.pop(i)
            rep_safe = is_safe(report)
            report.insert(i, l)

            if rep_safe:
                safe2 += 1
                break

    print(safe1)
    print(safe2)


if __name__ == "__main__":
    solution()
