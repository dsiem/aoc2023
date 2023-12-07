import functools
from collections.abc import Generator, Iterable, Sequence


def seed_map(
    seeds: Iterable[tuple[int, int]], maps: Sequence[tuple[int, int, int]]
) -> Generator[tuple[int, int], None, None]:
    for loc, num in seeds:
        for src, dst, length in maps:
            before = min(num, src - loc)
            if before > 0:
                yield loc, before
                loc, num = src, num - before
            inside = min(num, src + length - loc)
            if inside > 0:
                yield dst - src + loc, inside
                loc, num = src + length, num - inside
            if num < 1:
                break
        else:
            yield loc, num


seeds, *atlas = open(0).read().split("\n\n")
seeds = list(map(int, seeds.split()[1:]))
atlas = ((map(int, m.split()) for m in maps.splitlines()[1:]) for maps in atlas)
atlas = [sorted((src, dst, length) for dst, src, length in maps) for maps in atlas]
parts = zip(seeds, [1] * len(seeds)), zip(seeds[::2], seeds[1::2])


print(*(min(functools.reduce(seed_map, atlas, part))[0] for part in parts))
