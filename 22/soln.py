from collections import defaultdict
from itertools import pairwise

buyers = []
with open("input.txt") as file:
    for line in file:
        buyers.append(int(line.strip()))


def new_secret_number(s: int):
    s = s ^ (s << 6) % 16777216
    s = s ^ (s >> 5) % 16777216
    s = s ^ (s << 11) % 16777216
    return s


def part1():
    ans1 = 0
    for buyer in buyers:
        init_secret = buyer
        for i in range(2000):
            init_secret = new_secret_number(init_secret)
        ans1 += init_secret
    print(ans1)


def part2():
    ans2 = defaultdict(int)
    for s in buyers:
        nums = [s] + [s := new_secret_number(s) for _ in range(2000)]
        diffs = [b % 10 - a % 10 for a, b in pairwise(nums)]
        seen = set()
        for i in range(len(diffs) - 3):
            seq = tuple(diffs[i : i + 4])
            if seq not in seen:
                ans2[seq] += nums[i + 4] % 10
                seen.add(seq)
    print(max(ans2.values()))


if __name__ == "__main__":
    # part1()
    part2()
