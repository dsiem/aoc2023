import re


def value(line: str, digits: str = r"\d|one|two|three|four|five|six|seven|eight|nine") -> int:
    matches = re.search(rf"(?=({digits})).*({digits})", line).group(1, 2)
    ten, one = (int(m) if m.isdigit() else digits.split("|").index(m) for m in matches)
    return 10 * ten + one


print(*map(sum, zip(*((value(line, r"\d"), value(line)) for line in open(0)))))
