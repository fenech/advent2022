import sys

trees = []

for line in map(str.strip, sys.stdin):
    row = [int(c) for c in line]
    trees.append(row)

width = len(trees[0])
height = len(trees)
visible = set()
max_score = 0

for i in range(1, width - 1):
    for j in range(1, height - 1):
        house = trees[j][i]

        up = 0
        h = 0
        for u in range(j):
            tree = trees[j-u-1][i]
            up += 1
            if tree >= house:
                break

        down = 0
        h = 0
        for d in range(j+1, height):
            tree = trees[d][i]
            down += 1
            if tree >= house:
                break

        left = 0
        h = 0
        for l in range(i):
            tree = trees[j][i-l-1]
            left += 1
            if tree >= house:
                break

        right = 0
        h = 0
        for r in range(i+1, width):
            tree = trees[j][r]
            right += 1
            if tree >= house:
                break

        score = up * down * left * right
        if score > max_score:
            max_score = score

print(max_score)
