import math


def n_ways(time: int, distance: int) -> int:
    sqrt = math.sqrt(time**2 - 4 * distance - 4)
    return int(-(time - sqrt) // 2 + (time + sqrt) // 2 + 1)


p2, *p1 = zip(*((int("".join(line.split()[1:])), *map(int, line.split()[1:])) for line in open(0)))
print(math.prod(n_ways(time, distance) for time, distance in p1), n_ways(*p2))
