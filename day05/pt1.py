"""
    [V] [G]             [H]
[Z] [H] [Z]         [T] [S]
[P] [D] [F]         [B] [V] [Q]
[B] [M] [V] [N]     [F] [D] [N]
[Q] [Q] [D] [F]     [Z] [Z] [P] [M]
[M] [Z] [R] [D] [Q] [V] [T] [F] [R]
[D] [L] [H] [G] [F] [Q] [M] [G] [W]
[N] [C] [Q] [H] [N] [D] [Q] [M] [B]
 1   2   3   4   5   6   7   8   9
"""


import regex
import sys
stacks = [
    list(s) for s in [
        "NDMQBPZ",
        "CLZQMDHV",
        "QHRDVFZG",
        "HGDFN",
        "NFQ",
        "DQVZFBT",
        "QMTZDVSH",
        "MGFPNQ",
        "BWRM"
    ]
]


r"move (\d+) from (\d+) to (\d+)"

for line in sys.stdin:
    m = regex.match(r"move (\d+) from (\d+) to (\d+)", line)
    count = int(m.group(1))
    src = int(m.group(2)) - 1
    dst = int(m.group(3)) - 1

    crates = []
    for _ in range(count):
        crates.append(stacks[src].pop())

    stacks[dst].extend(crates)

print("".join(s[-1] for s in stacks))
