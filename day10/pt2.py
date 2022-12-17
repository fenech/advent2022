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

output = []
for cycle, ins in enumerate(expanded):
    cycle %= 40
    if cycle-1 <= x <= cycle+1:
        output.append("#")
    else:
        output.append(".")

    x += ins

for i in range(0, len(output), 40):
    print("".join(output[i:i+40]))
