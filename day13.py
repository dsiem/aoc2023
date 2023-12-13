def score(pattern: list[str], dist: int) -> int:
    for i in range(len(pattern)):
        diff = sum(a != b for x, y in zip(pattern[i - 1 :: -1], pattern[i:]) for a, b in zip(x, y))
        if diff == dist:
            return i
    return 0


patterns = [p.split() for p in open(0).read().split("\n\n")]
print(*(sum(100 * score(p, d) + score(list(zip(*p)), d) for p in patterns) for d in (0, 1)))
