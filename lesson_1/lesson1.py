# Lesson 1 | About the Class

# || Comments ||
# I feel my solution was very similar to the proposed solution in class. What I was trying to accomplish was pretty much
# the same thing the teacher tried, I was simply not aware of the list generation method and I feel I sort of over
# complicated a lit bit with the map and lambda stuff. It is what it is. I've learned now.
def ss(lst):
    list_squared_numbers = list(map(lambda x: x * x, lst))

    return sum(list_squared_numbers)

# print (ss([1, 2, 3]))

# Lesson 1 | Poker hand

cards = {'2' : 2,
         '3' : 3,
         '4' : 4,
         '5' : 5,
         '6' : 6,
         '7' : 7,
         '8' : 8,
         '9' : 9,
         '10' : 10,
         'J' : 11,
         'Q' : 12,
         'K' : 13,
         'A' : 14}


def get_value_from_card(card):
    global cards

    if card in cards:
        return cards[card]


def poker(hands):
    """Return the best hand: poker([hand, ...]) => hand"""
    return  max(hands, key=compute_rank)




def compute_rank(hand):
    if is_royal_flush(hand):
        return 10,
    elif is_flush(hand) and is_straight(hand):
        straight_flush_rank = get_value_from_card(highest_card_in_card(hand))
        return 9, straight_flush_rank
    elif is_n_kind(4, hand):
        """Each four of a kind is ranked first by the rank of its quadruplet, and then by the rank of its kicker."""
        quadruplet_rank = get_value_from_card(get_card_with_n_ocurrences(hand, 4))
        kicker_rank = get_value_from_card(get_card_with_n_ocurrences(hand, 1))

        return 8, quadruplet_rank, kicker_rank
    elif is_full_house(hand):
        """If two or more players have a full house then the player with the best three of a kind wins. If those are
        the same then the player with the best pair wins."""

        three_of_kind_rank = get_value_from_card(get_card_with_n_ocurrences(hand, 3))
        pair_rank = get_value_from_card(get_card_with_n_ocurrences(hand, 2))

        return 7, three_of_kind_rank, pair_rank
    elif is_flush(hand):
        """If two of more players share a flush then the player with the highest card (all the way to the fifth card
        if necessary) in the flush wins."""
        cards = [get_value_from_card(card) for card in get_all_numbers_from_hand(hand)]

        cards.sort(reverse=True)

        return 6, cards[0], cards[1], cards[2], cards[3], cards[4]
    elif is_straight(hand):
        """In the event of a tie: Highest ranking card at the top of the sequence wins."""
        return 5, get_value_from_card(highest_card_in_card(hand))
    elif is_n_kind(3, hand):
        """In the event of a tie: Highest ranking three of a kind wins. In community card games where players have the
        same three of a kind, the highest side card, and if necessary, the second-highest side card wins."""
        triplet_rank = get_value_from_card(get_card_with_n_ocurrences(hand, 3))
        highest_side_card = get_n_highest_side_card_from_3_kind(hand, 1)
        second_highest_side_card = get_n_highest_side_card_from_3_kind(hand, 2)

        return 4, triplet_rank, get_value_from_card(highest_side_card), get_value_from_card(second_highest_side_card)
    elif is_two_pair(hand):
        """In the event of a tie: Highest pair wins. If players have the same highest pair, highest second pair wins.
        If both players have two identical pairs, highest side card wins."""
        ocurrences = get_number_ocurrences_cards(hand)

        pairs = [card for card in ocurrences if ocurrences[card] == 2]
        pairs.sort(key=get_value_from_card, reverse=True)

        highest_pair = get_value_from_card(pairs[0])
        second_highest_pair = get_value_from_card(pairs[1])
        side_card = get_value_from_card([card for card in ocurrences if ocurrences[card] == 1][0])

        return 3, highest_pair, second_highest_pair, side_card
    elif is_n_kind(2, hand):
        pair_rank = get_value_from_card(get_card_with_n_ocurrences(hand, 2))

        ocurrences = get_number_ocurrences_cards(hand)

        remaining_cards = list(map(get_value_from_card, [card for card in ocurrences if ocurrences[card] != 2]))
        remaining_cards.sort(reverse=True)

        return 2, pair_rank, remaining_cards[0], remaining_cards[1], remaining_cards[2]
    else:
        cards = list(map(get_value_from_card, get_all_numbers_from_hand(hand)))
        cards.sort(reverse=True)

        return 1, cards[0], cards[1], cards[2], cards[3], cards[4]


def is_royal_flush(hand):
    """Combination of ten, jack, queen, king, ace, all of the same suit"""
    return contains_card('10', hand) and contains_card('J', hand) and contains_card('Q', hand) and contains_card('K', hand) \
        and contains_card('A', hand) and get_number_of_different_suits(hand) == 1


def is_n_kind(n, hand):
    return int(n) in get_number_ocurrences_cards(hand).values()


def is_full_house(hand):
    ocurrences = get_number_ocurrences_cards(hand)

    # There can only be 2 different numbers and they must happen 2 and 3 times, making a 3-kind and a pair.
    return len(set(get_all_numbers_from_hand(hand))) == 2 and (2 in ocurrences.values()) and (3 in ocurrences.values())


def is_flush(hand):
    """Five cards of the same suit, in any order"""
    return get_number_of_different_suits(hand) == 1


def is_straight(hand):
    """Five cards of any suit, in sequential order"""
    cards_numbers = sorted(get_all_numbers_from_hand(hand), key=lambda element: cards[element])

    cards_values = [cards[x] for x in cards_numbers]

    for i in range(1, len(cards_values)):
        if cards_values[i] != cards_values[i - 1] + 1:
            return False

    return True


def is_two_pair(hand):
    """Two different pairs in the same hand"""
    return list(get_number_ocurrences_cards(hand).values()).count(2) == 2


def contains_card(card, hand):
    return card in get_all_numbers_from_hand(hand)


def get_all_numbers_from_hand(hand):
    return [x[0] for x in hand]


def get_all_suits_from_hand(hand):
    return [x[1] for x in hand]


def get_number_of_different_suits(hand):
    return len(set(get_all_suits_from_hand(hand)))


def get_number_ocurrences_cards(hand):
    ocurrences = {}

    for card in hand:
        if card[0] in ocurrences:
            ocurrences[card[0]] += 1
        else:
            ocurrences[card[0]] = 1

    return ocurrences


# Helpers


def highest_card_in_card(hand):
    return max([x[0] for x in hand], key=get_value_from_card)


def get_card_with_n_ocurrences(hand, times):
    ocurrences = get_number_ocurrences_cards(hand)

    for card in ocurrences:
        if ocurrences[card] == times:
            return card


def get_n_highest_side_card_from_3_kind(hand, n):
    ocurrences = get_number_ocurrences_cards(hand)

    side_cards = [card for card in ocurrences if ocurrences[card] != 3]

    if len(side_cards) != 2:
        print('Hand was not a 3-kind!')
        return

    side_cards.sort(key=get_value_from_card)

    return side_cards[len(side_cards) - n]

royal_flush_hand = [('J', 'D'), ('10', 'D'), ('Q', 'D'), ('K', 'D'), ('A', 'D')]
same_suit_hand = [('2', 'D'), ('5', 'D'), ('Q', 'D'), ('7', 'D'), ('3', 'D')]
straight_flush_hand = [('5', 'S'), ('6', 'S'), ('7', 'S'), ('8', 'S'), ('9', 'S')]
straight_flush_hand_2 = [('6', 'C'), ('5', 'C'), ('4', 'C'), ('3', 'C'), ('2', 'C')]
straight_flush_hand_3 = [('9', 'S'), ('10', 'S'), ('J', 'S'), ('Q', 'S'), ('K', 'S')]
four_kind = [('6', 'D'), ('6', 'C'), ('6', 'S'), ('6', 'C'), ('3', 'H')]
four_kind_2 = [('6', 'D'), ('6', 'C'), ('6', 'S'), ('6', 'C'), ('2', 'H')]
four_kind_3 = [('9', 'D'), ('9', 'C'), ('9', 'S'), ('9', 'C'), ('2', 'H')]
three_kind = [('9', 'D'), ('9', 'C'), ('9', 'S'), ('8', 'C'), ('2', 'H')]

# Full-house
full_house = [('J', 'D'), ('J', 'C'), ('J', 'S'), ('2', 'C'), ('2', 'H')]
full_house_2 = [('5', 'D'), ('9', 'C'), ('5', 'S'), ('9', 'C'), ('9', 'H')]

# Flush
flush = [('5', 'H'), ('8', 'H'), ('10', 'H'), ('J', 'H'), ('A', 'H')]

# 2-Pair
two_pair = [('4', 'h'), ('7', 'H'), ('7', 'D'), ('J', 'C'), ('J', 'H')]

hands = [four_kind_2, four_kind, four_kind_3]

# print(poker(hands))
