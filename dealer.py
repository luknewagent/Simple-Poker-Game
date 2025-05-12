class Dealer:
    def __init__(self):
        self.deck = None

    def set_deck(self, deck):
        self.deck = deck.deck

    def deal_cards(self, n, hand):
        for i in range(n):
            hand.append(self.deck.pop())
