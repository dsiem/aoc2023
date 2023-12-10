import operator
from collections.abc import Iterable
from functools import reduce
from itertools import accumulate


def diagonal(nums: Iterable[int], next: int) -> Iterable[int]:
    return accumulate(nums, operator.__sub__, initial=next)


def succ(nums: Iterable[int]) -> int:
    return sum(reduce(diagonal, nums, []))


parts = ([succ(map(int, line.split()[::dir])) for dir in (1, -1)] for line in open(0))
print(*map(sum, zip(*parts)))
