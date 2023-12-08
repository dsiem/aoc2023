def parse(line: str, jokers: bool = False) -> tuple:
    hand, bid = line.split()
    hand = hand.translate(str.maketrans("TJQKA", ("ABCDE", "A0CDE")[jokers]))
    hand = hand.replace("0", max(hand, key=hand.count))
    value = sum(map(hand.count, hand))
    return value, hand, bid


for part in zip(*((parse(line), parse(line, jokers=True)) for line in open(0))):
    print(sum(rank * int(bid) for rank, (_best, _hand, bid) in enumerate(sorted(part), 1)))
