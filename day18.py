from collections.abc import Callable


def part1(d: str, n: str, c: str) -> tuple[str, int]:
    return 1j ** (ord(d) % 15), int(n)


def part2(d: str, n: str, c: str) -> tuple[str, int]:
    return 1j ** int(c[-2]), int(c[2:-2], 16)


def solve(fn: Callable[[str], tuple[str, int]]) -> int:
    x = a = b = 0
    for line in lines:
        d, n = fn(*line.split())
        x += n * d.imag
        a += n * d.real * x
        b += n

    return int(abs(a) + b / 2 + 1)


lines = open(0).readlines()
print(*map(solve, (part1, part2)))
