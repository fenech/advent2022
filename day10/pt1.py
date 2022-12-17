import sys

x = 1
total = 0


def process(ins):
    if ins.startswith("noop"):
        yield 0
    else:
        yield 0
        _, count = ins.split()
        yield int(count)


expanded = (
    count for line in sys.stdin for count in process(line)
)

for cycle, ins in enumerate(expanded, 1):
    if cycle % 40 == 20:
        total += cycle * x

    x += ins

print(total)
