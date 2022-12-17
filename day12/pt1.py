import sys
from collections import namedtuple


lines = sys.stdin.read().splitlines()
width = len(lines[0])
height = len(lines)

grid = []

Point = namedtuple('Point', 'x y')

for j, line in enumerate(lines):
    cells = []
    for i, c in enumerate(line):
        cells.append(c)
        if c == "S":
            start = Point(i, j)
        elif c == "E":
            end = Point(i, j)
    grid.append(cells)


def elevation(grid, point):
    c = grid[point.y][point.x]
    if c == "S":
        c = "a"
    elif c == "E":
        c = "z"
    return ord(c)


def in_grid(p: Point):
    return p.x >= 0 and p.x < width and p.y >= 0 and p.y < height


def steppable(grid, p1: Point, p2: Point):
    return elevation(grid, p2) - elevation(grid, p1) <= 1


def possible_moves(grid, point: Point):
    moves = (
        Point(point.x + 1, point.y),
        Point(point.x - 1, point.y),
        Point(point.x, point.y + 1),
        Point(point.x, point.y - 1),
    )

    return filter(lambda p: in_grid(p) and steppable(grid, point, p), moves)


current = {start}
visited = set()
steps = 0

while end not in current:
    next_steps = set()
    for point in current:
        for move in possible_moves(grid, point):
            if move in visited:
                continue
            visited.add(move)
            next_steps.add(move)
    steps += 1
    current = next_steps
print(steps)
