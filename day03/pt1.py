import sys


def priority(c):
    if c < "a":
        return ord(c) - 38
    else:
        return ord(c) - 96


total = 0
for line in sys.stdin:
    s = line.strip()
    a, = set(s[:len(s)//2]) & set(s[len(s)//2:])
    total += priority(a)

print(total)
