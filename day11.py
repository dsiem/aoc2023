from collections.abc import Sequence


def sums(seq: Sequence[int], exp: int) -> int:
    it = enumerate(zip(seq, seq[1:]), 1)
    return sum(i * (len(seq) - i) * (1 + max(0, b - a - 1) * exp) for i, (a, b) in it if a != b)


xs, ys = zip(*((x, y) for y, line in enumerate(open(0)) for x, c in enumerate(line) if c == "#"))
xs = sorted(xs)
print(sums(xs, 2) + sums(ys, 2), sums(xs, 1_000_000) + sums(ys, 1_000_000))
