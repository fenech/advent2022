import sys
import regex

fs = {}
cwd = []

lines = map(str.strip, sys.stdin)

for line in lines:
    if line.startswith("$"):
        cmd = line[2:]
        if m := regex.match(r"cd (.+)", cmd):
            path = m.group(1)
            if path == "/":
                cwd = []
            elif path == "..":
                cwd.pop()
            else:
                cwd.append(path)
        continue

    if line.startswith("dir"):
        continue

    size, name = line.split(" ")

    for i, part in enumerate(cwd):
        d = "/".join(cwd[:i+1])
        fs[d] = fs.get(d, 0) + int(size)

total = 0
for d in fs:
    if fs[d] < 100000:
        total += fs[d]

print(total)
