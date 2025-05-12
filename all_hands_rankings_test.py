from card import Card, show_hand
from ranks import find_ranking


royal_flush = [Card(14, 'S'), Card(13, 'S'), Card(12, 'S'), Card(
    11, 'S'), Card(10, 'S')]
straight_flush = [Card(14, 'S'), Card(2, 'S'), Card(3, 'S'), Card(
    4, 'S'), Card(5, 'S')]
four_of_a_kind = [Card(14, 'S'), Card(14, 'H'), Card(14, 'D'), Card(
    14, 'C'), Card(13, 'S')]
full_house = [Card(14, 'S'), Card(14, 'H'), Card(14, 'D'), Card(
    13, 'S'), Card(13, 'H')]
flush = [Card(14, 'S'), Card(2, 'S'), Card(9, 'S'), Card(
    4, 'S'), Card(5, 'S')]
straight = [Card(14, 'C'), Card(2, 'S'), Card(3, 'S'), Card(
    4, 'H'), Card(5, 'S')]
three_of_a_kind = [Card(14, 'S'), Card(14, 'H'), Card(14, 'D'), Card(
    13, 'S'), Card(12, 'S')]
two_pair = [Card(14, 'S'), Card(14, 'H'), Card(
    13, 'S'), Card(12, 'S'), Card(12, 'H')]
one_pair = [Card(14, 'S'), Card(14, 'H'), Card(
    13, 'S'), Card(12, 'S'), Card(11, 'S')]

hands = [royal_flush, straight_flush, four_of_a_kind, full_house,
         flush, straight, three_of_a_kind, two_pair, one_pair]

for hand in hands:
    print(find_ranking(hand))
    show_hand(hand)