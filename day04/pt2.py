import sys


def sections(e):
    start, end = e.split("-")
    return range(int(start), int(end)+1)


total = 0

for line in sys.stdin:
    s = line.strip()
    e1, e2 = s.split(",")
    r1 = set(sections(e1))
    r2 = set(sections(e2))
    if r1 & r2:
        total += 1

print(total)
