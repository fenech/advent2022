import sys


def sections(e):
    start, end = e.split("-")
    return range(int(start), int(end)+1)


total = 0

for line in sys.stdin:
    s = line.strip()
    e1, e2 = s.split(",")
    r1 = sections(e1)
    r2 = sections(e2)
    if (r1.start in r2 and r1[-1] in r2) or r2.start in r1 and r2[-1] in r1:
        total += 1

print(total)
