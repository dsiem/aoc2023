import collections
import re
from math import prod

schematic = open(0).read()
symbols = {i for i, c in enumerate(schematic) if c not in "01234567890.\n"}
parts = collections.defaultdict(list)

for m in re.finditer(r"\d+", schematic):
    interval = range(m.start() - 1, m.end() + 1)
    for i in symbols & {i + row_shift for i in interval for row_shift in (-141, 0, 141)}:
        parts[i].append(int(m.group()))

print(*map(sum, zip(*((sum(p), prod(p) * (len(p) == 2)) for p in parts.values()))))
