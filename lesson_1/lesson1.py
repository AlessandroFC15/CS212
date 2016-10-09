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


def poker(hands):
    global cards

    hands_ranks = {}

    """Return the best hand: poker([hand, ...]) => hand"""
    # 1st step => Calculate rankings for each hand
    for i in range(0, len(hands)):
        hand = hands[i]

        if is_royal_flush(hand):
            hands_ranks[i] = 1
        elif is_straight_flush(hand, cards):
            hands_ranks[i] = 2
        elif is_n_kind(4, hand):
            hands_ranks[i] = 3
        elif is_full_house(hand):
            hands_ranks[i] = 4
        elif is_flush(hand):
            hands_ranks[i] = 5
        elif is_straight(hand):
            hands_ranks[i] = 6
        elif is_n_kind(3, hand):
            hands_ranks[i] = 7
        elif is_two_pair(hand):
            hands_ranks[i] = 8
        elif is_n_kind(2, hand):
            hands_ranks[i] = 9
        # elif is_high_card(hand):
        #     print('HighCard')
        else:
            hands_ranks[i] = 10

    highest_ranked_card_index = min(hands_ranks.keys(), key=(lambda key: hands_ranks[key]))

    return hands[highest_ranked_card_index]

    # 2nd step => Return the highest one


def is_royal_flush(hand):
    """Combination of ten, jack, queen, king, ace, all of the same suit"""
    return contains_card('10', hand) and contains_card('J', hand) and contains_card('Q', hand) and contains_card('K', hand) \
        and contains_card('A', hand) and get_number_of_different_suits(hand) == 1


def is_straight_flush(hand, cards):
    return is_flush(hand) and is_straight(hand)


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

royal_flush_hand = [('J', 'D'), ('10', 'D'), ('Q', 'D'), ('K', 'D'), ('A', 'D')]
same_suit_hand = [('2', 'D'), ('5', 'D'), ('Q', 'D'), ('7', 'D'), ('3', 'D')]
straight_flush_hand = [('5', 'S'), ('6', 'S'), ('7', 'S'), ('8', 'S'), ('9', 'S')]
straight_flush_hand_2 = [('6', 'C'), ('5', 'C'), ('4', 'C'), ('3', 'C'), ('2', 'C')]
four_kind = [('6', 'D'), ('6', 'C'), ('6', 'S'), ('6', 'C'), ('2', 'H')]

# Full-house
full_house = [('J', 'D'), ('J', 'C'), ('J', 'S'), ('2', 'C'), ('2', 'H')]
full_house_2 = [('5', 'D'), ('9', 'C'), ('5', 'S'), ('9', 'C'), ('9', 'H')]

# Flush
flush = [('5', 'H'), ('8', 'H'), ('10', 'H'), ('J', 'H'), ('A', 'H')]

# 2-Pair
two_pair = [('4', 'h'), ('7', 'H'), ('7', 'D'), ('J', 'C'), ('J', 'H')]

hands = [royal_flush_hand, flush, full_house]

print(poker(hands))