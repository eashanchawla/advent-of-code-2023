from card import *
from pathlib import Path
parent_path = Path(__file__).parent
with open(parent_path/'d4.txt', 'r') as f:
    data=f.readlines()

data = [x.strip() for x in data]
cards = [Card(x) for x in data]
points = [card.calculate_score() for card in cards]
print(f'Part 1: {sum(points)}')

cards_found = [1 for _ in range(len(cards))]
for i, card in enumerate(cards):
    for j in range(card.matches):
        cards_found[i+j+1]+=cards_found[i]

print(f'Part 2: {sum(cards_found)}')