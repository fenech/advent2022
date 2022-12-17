import sys
import itertools


def priority(c):
    if c < "a":
        return ord(c) - 38
    else:
        return ord(c) - 96


total = 0

while True:
    group = [set(sys.stdin.readline().strip()) for _ in range(3)]
    try:
        badge,  = group[0] & group[1] & group[2]
    except ValueError:
        break
    total += priority(badge)

print(total)
