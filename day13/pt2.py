from functools import cmp_to_key
import sys
import json


def cmp(la, lb):
    for a, b in zip(la, lb):
        if isinstance(a, int) and isinstance(b, int):
            if a != b:
                return a - b
        else:
            a = a if isinstance(a, list) else [a]
            b = b if isinstance(b, list) else [b]
            if c := cmp(a, b):
                return c

    return len(la) - len(lb)


total = 0
lines = sys.stdin.readlines()
packets = list(map(json.loads, lines[::3] + (lines[1::3]))) + [[[2]], [[6]]]

packets.sort(key=cmp_to_key(cmp))
for p in packets:
    print(p)

key = 1
for i, p in enumerate(packets, 1):
    if len(p) == 1 and isinstance(p[0], list) and len(p[0]) == 1 and p[0][0] in (2, 6):
        print(i)
        key *= i

print(key)
