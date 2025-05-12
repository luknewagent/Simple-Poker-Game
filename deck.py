import random

from card import Card


class Deck:
    def __init__(self):
        self.deck = [Card(rank, suit) for rank in range(2, 15)
                     for suit in ["S", "H", "D", "C"]]
        random.shuffle(self.deck)

    def pop(self):
        self.deck.pop()
