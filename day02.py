import collections
import functools
import operator
import re

threshold = collections.Counter({"r": 12, "g": 13, "b": 14})


def solve(i: int, line: str) -> tuple[int, int]:
    cnt = (collections.Counter({color: int(num)}) for num, color in re.findall(r"(\d+) (\w)", line))
    max = functools.reduce(operator.or_, cnt)
    return (max <= threshold) * i, functools.reduce(operator.mul, max.values())


print(*map(sum, zip(*(solve(i, line) for i, line in enumerate(open(0), 1)))))
