wins = [len(set(line[10:40].split()) & set(line[42:].split())) for line in open(0)]

cards = [1] * len(wins)
for i, n in enumerate(wins):
    for j in range(n):
        cards[1 + i + j] += cards[i]

print(sum(round(2 ** (n - 1)) for n in wins), sum(cards))
