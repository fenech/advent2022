import sys
import regex

"""
Monkey 0:
  Starting items: 66, 59, 64, 51
  Operation: new = old * 3
  Test: divisible by 2
    If true: throw to monkey 1
    If false: throw to monkey 4
"""


class Monkey:
    inspections = 0

    def __init__(self, m):
        _, items, operation, test, yes, no = m.splitlines()
        self.items = list(map(int, regex.findall(r"(\d+)", items)))
        op = regex.search(r"new = (old.*)", operation)
        self.operation = eval("lambda old: " + op.group(1))
        t = regex.search(r"(\d+)", test)
        self.div = int(t.group(1))
        self.yes = int(regex.search(r"monkey (\d+)", yes).group(1))
        self.no = int(regex.search(r"monkey (\d+)", no).group(1))


monkeys = [Monkey(monkey) for monkey in sys.stdin.read().split("\n\n")]

lcd = 1
for m in monkeys:
    lcd *= m.div

for round in range(10000):
    for m in monkeys:
        while len(m.items):
            m.inspections += 1
            item = m.items.pop(0)
            item = m.operation(item) % lcd
            if item % m.div == 0:
                monkeys[m.yes].items.append(item)
            else:
                monkeys[m.no].items.append(item)

m1, m2 = sorted(monkeys, key=lambda m: m.inspections, reverse=True)[:2]
print(m1.inspections*m2.inspections)
