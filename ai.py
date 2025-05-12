from collections import Counter
from ranks import Rank, find_ranking


def ai_eval_for_lasting_friends(hand) -> list:
    # this function returns the cards that are the best to keep for the machine
    values = [card.value for card in hand]
    values_counts = Counter(values)
    rank = find_ranking(hand)

    lasting_friends = []
    if rank == Rank.HIGH_CARD:
        lasts = -1
        good_highs = [card for card in hand if card.get_value() > 10]

        if [card.value for card in good_highs] == [13, 14]:
            lasts = -2

        lasting_friends = good_highs[lasts::]

    elif rank == Rank.TWO_PAIRS:
        pairs = [card for card in hand if values_counts[card.value] == 2]
        highest_pair = pairs[-2::]
        lasting_friends = highest_pair
    elif rank in [Rank.THREE_OF_A_KIND, Rank.PAIR]:
        lasting_friends = [
            card for card in hand if values_counts[card.value] >= 2]
    return lasting_friends
