def parse(line: str, jokers: bool = False) -> tuple[int, str, int]:
    hand, bid = line.split()
    hand = hand.translate(str.maketrans("TJQKA", ("ABCDE", "A0CDE")[jokers]))
    best_hand = hand.replace("0", max(hand, key=hand.replace("0", "").count))
    value = sum(map(best_hand.count, best_hand))
    return value, hand, int(bid)


for part in zip(*((parse(line), parse(line, jokers=True)) for line in open(0))):
    print(sum(rank * bid for rank, (_value, _hand, bid) in enumerate(sorted(part), 1)))
