import itertools
import math

dirs, _, *ways = open(0).read().splitlines()
ways = {way[0:3]: (way[7:10], way[12:15]) for way in ways}


def walk(pos: str) -> int:
    for i, dir in enumerate(itertools.cycle(dirs)):
        if pos.endswith("Z"):
            return i
        pos = ways[pos][dir == "R"]
    raise RuntimeError("unreachable")


print(walk("AAA"), math.lcm(*(walk(way) for way in ways if way.endswith("A"))))
