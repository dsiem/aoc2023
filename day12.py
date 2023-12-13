import functools
import re


def solve(line: str, factor: int = 1) -> int:
    springs, nums = line.split()
    springs = f"{springs}?" * factor
    nums = tuple(map(int, nums.split(","))) * factor

    @functools.cache
    def count(sub: str, nums: tuple[int]) -> int:
        if not sub:
            return not nums
        ans = count(sub[1:], nums) if sub[0] != "#" else 0
        if nums and re.match(rf"[#?]{{{nums[0]}}}[.?]", sub):
            ans += count(sub[nums[0] + 1 :], nums[1:])
        return ans

    return count(springs, nums)


print(*map(sum, zip(*((solve(line), solve(line, 5)) for line in open(0)))))
