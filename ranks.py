from collections import Counter
from enum import Enum


class Rank(Enum):
    ROYAL_FLUSH = 8
    STRAIGHT_FLUSH = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    FLUSH = 4
    STRAIGHT = 3
    THREE_OF_A_KIND = 2
    TWO_PAIRS = 1
    PAIR = 0
    HIGH_CARD = -1


def is_pair(hand):
    values = [card.get_value() for card in hand]
    values_counts = Counter(values)
    if any(value == 2 for value in values_counts.values()):
        return Rank.PAIR


def is_two_pairs(hand):
    values = [card.get_value() for card in hand]
    values_counts = Counter(values)
    if list(values_counts.values()).count(2) == 2:
        return Rank.TWO_PAIRS


def is_three_of_a_kind(hand):
    values = [card.get_value() for card in hand]
    values_counts = Counter(values)
    if any(value == 3 for value in values_counts.values()):
        return Rank.THREE_OF_A_KIND


def is_straight(hand):
    values = [card.get_value() for card in hand]
    if values == list(range(values[0], values[0]+5)):
        return Rank.STRAIGHT


def is_flush(hand):
    suits = [card.get_suit() for card in hand]
    if len(set(suits)) != 1:
        return False


def is_full_house(hand):
    values = [card.get_value() for card in hand]
    values_counts = Counter(values)
    if sorted(list(values_counts.values())) == [2, 3]:
        return Rank.FULL_HOUSE


def is_four_of_a_kind(hand):
    values = [card.get_value() for card in hand]
    values_counts = Counter(values)
    if any(value == 4 for value in values_counts.values()):
        return Rank.FOUR_OF_A_KIND


def is_straight_flush(hand):
    values = [card.get_value() for card in hand]
    suits = [card.get_suit() for card in hand]

    if len(set(suits)) != 1:
        return False
    if values == list(range(values[0], values[0]+5)):
        return Rank.STRAIGHT_FLUSH
    return False


def is_royal_flush(hand):
    values = [card.get_value() for card in hand]
    suits = [card.get_suit() for card in hand]
    if not is_flush(hand):
        return False
    if values == [10, 11, 12, 13, 14]:
        return Rank.ROYAL_FLUSH


ranking_list = [is_royal_flush, is_straight_flush, is_four_of_a_kind,
                is_full_house, is_flush, is_straight, is_three_of_a_kind, is_two_pairs, is_pair]


def find_ranking(hand):
    hand.sort(key=lambda x: x.value)
    for rank_func in ranking_list:
        found_rank = rank_func(hand)
        if found_rank:
            return found_rank
    return Rank.HIGH_CARD
