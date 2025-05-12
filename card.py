class Card:
    _value_map = {"14": "A", "13": "K", "12": "Q", "11": "J"}

    def __init__(self, value, suit) -> None:
        self.value = int(value)
        self.symbol = self._value_map.get(str(value), str(value))
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit


def eval_ace_value(hand):
    hand.sort(key=lambda x: x.value)
    if [2, 3, 4, 5, 14] == [card.value for card in hand]:
        ace = hand.pop()
        ace.value = 1
        hand.insert(0, ace)
    return hand


def show_hand(hand):
    hand.sort(key=lambda x: x.value)
    for card in hand:
        print(card.symbol + card.suit, end=' ')
    print()
