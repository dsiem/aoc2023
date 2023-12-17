import heapq

grid = {(a, b): int(c) for b, line in enumerate(open(0)) for a, c in enumerate(line.strip())}


def min_heat(ran: range, stop: tuple[int, int] = max(grid)) -> int | None:
    heap, seen = [(0, (1, 0), (0, 0)), (0, (0, 1), (0, 0))], set()
    while heap:
        heat, dir, pos = _, (dx, dy), (x, y) = heapq.heappop(heap)
        if pos == stop:
            return heat
        if (pos, dir) in seen:
            continue
        seen.add((pos, dir))
        for dir_ in (dy, dx), (-dy, -dx):
            for n in ran:
                if (pos_ := (x + n * dx, y + n * dy)) in grid:
                    heat_ = heat + sum(grid[x + m * dx, y + m * dy] for m in range(1, n + 1))
                    heapq.heappush(heap, (heat_, dir_, pos_))
    return None


print(*map(min_heat, (range(1, 4), range(4, 11))))
