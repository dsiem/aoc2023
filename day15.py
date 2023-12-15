import collections
import functools
import re


def hash(s: str) -> int:
    return functools.reduce(lambda h, c: (h + ord(c)) * 17 % 256, s, 0)


data = open(0).read().strip()
result = sum(map(hash, data.split(",")))

boxes = collections.defaultdict(dict)
for m in re.findall(r"(\w+)[=-](\d?)", data):
    match m:
        case label, "":
            boxes[hash(label)].pop(label, 0)
        case label, focal:
            boxes[hash(label)][label] = int(focal)

print(result, sum((h + 1) * i * f for h, b in boxes.items() for i, f in enumerate(b.values(), 1)))
