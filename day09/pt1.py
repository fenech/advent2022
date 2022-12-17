import sys


def process(ins):
    d, n = ins.split()
    for _ in range(int(n)):
        yield d


expanded = (
    move for line in sys.stdin for move in process(line)
)

h = (0, 0)
t = (0, 0)

covered = set()

for d in expanded:
    hx, hy = h
    if d == "U":
        h = (hx, hy+1)
    elif d == "D":
        h = (hx, hy-1)
    elif d == "L":
        h = (hx-1, hy)
    elif d == "R":
        h = (hx+1, hy)

    hx, hy = h
    tx, ty = t

    dx = hx - tx
    dy = hy - ty

    if abs(dx)+abs(dy) > 2:
        t = (tx+dx//abs(dx), ty+dy//abs(dy))
    elif abs(dx) > 1:
        t = (tx+dx//abs(dx), ty)
    elif abs(dy) > 1:
        t = (tx, ty+dy//abs(dy))

    print(h, t)

    covered.add(t)

print(len(covered))
