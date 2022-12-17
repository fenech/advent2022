import sys
import json


def cmp(la, lb):
    for a, b in zip(la, lb):
        if isinstance(a, int) and isinstance(b, int):
            if a != b:
                return a < b
        else:
            a = a if isinstance(a, list) else [a]
            b = b if isinstance(b, list) else [b]
            c = cmp(a, b)
            if c is not None:
                return c
    if len(la) != len(lb):
        return len(la) < len(lb)


total = 0
lines = sys.stdin.readlines()
pairs = zip(lines[::3], lines[1::3])
for i, p in enumerate(pairs, 1):
    la, lb = map(json.loads, p)
    if cmp(la, lb):
        total += i

print(total)
