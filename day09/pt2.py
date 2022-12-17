import sys


def process(ins):
    d, n = ins.split()
    for _ in range(int(n)):
        yield d


expanded = (
    move for line in sys.stdin for move in process(line)
)

knots = [(0, 0) for _ in range(10)]

covered = set()

for d in expanded:
    hx, hy = knots[0]
    if d == "U":
        h = (hx, hy+1)
    elif d == "D":
        h = (hx, hy-1)
    elif d == "L":
        h = (hx-1, hy)
    elif d == "R":
        h = (hx+1, hy)
    knots[0] = h

    for i, t in enumerate(knots[1:], 1):
        hx, hy = knots[i-1]
        tx, ty = t

        dx = hx - tx
        dy = hy - ty

        if abs(dx)+abs(dy) > 2:
            t = (tx+dx//abs(dx), ty+dy//abs(dy))
        elif abs(dx) > 1:
            t = (tx+dx//abs(dx), ty)
        elif abs(dy) > 1:
            t = (tx, ty+dy//abs(dy))
        knots[i] = t

    covered.add(t)

print(len(covered))
