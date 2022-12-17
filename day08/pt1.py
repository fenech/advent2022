import sys

trees = []

for line in map(str.strip, sys.stdin):
    row = [int(c) for c in line]
    trees.append(row)

width = len(trees[0])
height = len(trees)
visible = set()

# looking from the left
for j in range(height):
    h = 0
    for i in range(width):
        t = trees[j][i]
        if i == 0 or t > h:
            h = t
            visible.add((i, j))

# looking from the right
for j in range(height):
    h = 0
    for i in range(width):
        t = trees[j][-i-1]
        if i == 0 or t > h:
            h = t
            visible.add((width-i-1, j))


# looking from the top
for i in range(width):
    h = 0
    for j in range(height):
        t = trees[j][i]
        if j == 0 or t > h:
            h = t
            visible.add((i, j))

# looking from the bottom
for i in range(width):
    h = 0
    for j in range(height):
        t = trees[-j-1][i]
        if j == 0 or t > h:
            h = t
            visible.add((i, height-j-1))

print(len(visible))
