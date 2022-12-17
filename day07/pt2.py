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


disk = 70000000
required = 30000000

try:
    du = fs[""]
except KeyError:
    du = 0
    for d in fs:
        if d.find("/") != -1:
            continue
        du += fs[d]


for d in sorted(fs, key=lambda x: fs[x]):
    print(d, fs[d])
    if fs[d] > required - (disk - du):
        break

print(fs[d])
