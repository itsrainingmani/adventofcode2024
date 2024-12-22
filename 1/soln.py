from collections import Counter


inputs = []
with open("input.txt") as file:
    for line in file:
        inputs.append(list(map(int, line.strip().split("   "))))


def solution():
    f = list(zip(*inputs))[0]
    s = list(zip(*inputs))[1]
    ans1 = sum([abs(a - b) for a, b in zip(sorted(f), sorted(s))])
    print(ans1)

    sc = Counter(s)
    ans2 = sum([i * sc[i] for i in f])
    print(ans2)


if __name__ == "__main__":
    solution()
