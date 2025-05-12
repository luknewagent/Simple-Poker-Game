from collections import Counter
from ai import ai_eval_for_lasting_friends
from card import show_hand, eval_ace_value
from dealer import Dealer
from deck import Deck
from ranks import Rank, find_ranking


def who_wins_high_card(player_hand, ai_hand):
    tied = True
    player_hand.sort(key=lambda x: x.value, reverse=True)
    ai_hand.sort(key=lambda x: x.value, reverse=True)
    for player_card, ai_card in zip(player_hand, ai_hand):
        if player_card.value > ai_card.value:
            print(f"player won with higher card {
                player_card.symbol} against {ai_card.symbol}")
            tied = False
            break
        elif player_card.value < ai_card.value:
            print(f"ai won with higher card {
                player_card.symbol} against {ai_card.symbol}")
            tied = False
            break
    if tied:
        print("There was a tie")


while True:
    deck = Deck()
    dealer = Dealer()
    dealer.set_deck(deck)

    player_hand = []
    ai_hand = []
    dealer.deal_cards(5, ai_hand)
    dealer.deal_cards(5, player_hand)

    print("-" * 35)
    print("AI\t= ", end=" ")
    show_hand(ai_hand)
    print("-" * 35)
    print("P\t= ", end=" ")
    show_hand(player_hand)
    print("-" * 35)

    # Change Option
    while True:
        change = input("Do you want to change cards? (y/n) ")
        if change.lower() == 'y':
            print("which card(s) do you want to change? enter positions (1-5)")
            print("example: 123")
            change_cards = list(int(x) - 1 for x in input(">"))

            if len(change_cards) > 5 or len(change_cards) < 1 or any(x < 0 or x > 4 for x in change_cards):
                print("Invalid input. Please enter 1-5 cards.")
                continue

            new_hand = [player_hand[change_cards[i]]
                        for i in range(len(change_cards))]
            for card in new_hand:
                player_hand.remove(card)
            dealer.deal_cards(len(new_hand), player_hand)
            break
        elif change.lower() == 'n':
            break

    ai_hand = ai_eval_for_lasting_friends(ai_hand)
    print(f"ai changed {5 - len(ai_hand)} card(s)")
    dealer.deal_cards(5 - len(ai_hand), ai_hand)

    player_hand = eval_ace_value(player_hand)
    ai_hand = eval_ace_value(ai_hand)

    ai_rank = find_ranking(ai_hand)
    player_rank = find_ranking(player_hand)
    print("-" * 35)
    print("AI\t= ", end=" ")
    show_hand(ai_hand)
    print("-" * 35)
    print("P\t= ", end=" ")
    show_hand(player_hand)
    print("-" * 35)

    if player_rank.value > ai_rank.value:
        print(f"player 1 won with {player_rank.name} against {ai_rank.name}")
    elif player_rank.value < ai_rank.value:
        print(f"ai won with {ai_rank.name} against {player_rank.name}")
    elif player_rank.value == ai_rank.value:
        player_values = [card.value for card in player_hand]
        ai_values = [card.value for card in ai_hand]
        player_counts = Counter(player_values)
        ai_counts = Counter(ai_values)
        if player_rank == Rank.PAIR:
            player_pair = max(player_counts.keys(),
                              key=lambda x: player_counts[x])
            ai_pair = max(ai_counts.keys(),
                          key=lambda x: player_counts[x])

            if player_pair > ai_pair:
                print(f"player won with higher {
                    player_rank.name}")
            elif player_pair < ai_pair:
                print(f"ai won with higher pair {
                    ai_rank.name}")

        elif player_rank == Rank.TWO_PAIRS:
            player_pair = max(player_counts.keys(),
                              key=lambda x: player_counts[x])
            ai_pair = max(ai_counts.keys(),
                          key=lambda x: ai_counts[x])

            if player_pair > ai_pair:
                print(f"player won with higher pair {
                    player_rank.name}")
            elif player_pair < ai_pair:
                print(f"ai won with higher {ai_rank.name}")

        elif player_rank in [Rank.FULL_HOUSE, Rank.FOUR_OF_A_KIND, Rank.THREE_OF_A_KIND]:
            player_three = max(player_counts.keys(),
                               key=lambda x: player_counts[x])
            ai_three = max(ai_counts.keys(),
                           key=lambda x: player_counts[x])
            if player_three > ai_three:
                print(f"player won with higher {
                    player_rank.name}")
            else:
                print(f"ai won with higher {
                    ai_rank.name}")
        elif player_rank in [Rank.STRAIGHT, Rank.STRAIGHT_FLUSH]:
            if player_values[-1] > ai_values[-1]:
                print(f"player won with higher {
                    player_rank.name}")
            elif player_values[-1] < ai_values[-1]:
                print(f"ai won with higher {
                    ai_rank.name}")
        else:
            who_wins_high_card(player_hand, ai_hand)

    print()
    print("-" * 35)
    print("want to play again? (y/n)")
    play_again = input("> ")
    if play_again.lower() == 'y':
        continue
    else:
        break
    print("-" * 35)
    print("\n" * 20)
