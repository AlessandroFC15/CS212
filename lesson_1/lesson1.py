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

    """Return the best hand: poker([hand, ...]) => hand"""
    # 1st step => Calculate rankings for each hand
    for hand in hands:
        if is_royal_flush(hand):
            print("Royal flush, brother!")
        elif is_straight_flush(hand, cards):
            print('SF')
        elif is_n_kind(4, hand):
            print('4Kind')
        elif is_full_house(hand):
            print("Full house")
        elif is_flush(hand):
            print('Flush')
        elif is_straight(hand):
            print("Straight")
        elif is_n_kind(3, hand):
            print("3Kind")
        elif is_two_pair(hand):
            print('2Pair')
        elif is_n_kind(2, hand):
            print("1Pair")
        elif is_high_card(hand):
            print('HighCard')
        else:
            print('Que mão horrível')

    # 2nd step => Return the highest one


def is_royal_flush(hand):
    """Combination of ten, jack, queen, king, ace, all of the same suit"""
    return contains_card('10', hand) and contains_card('J', hand) and contains_card('Q', hand) and contains_card('K', hand) \
        and contains_card('A', hand) and get_number_of_different_suits(hand) == 1


def is_straight_flush(hand, cards):
    if get_number_of_different_suits(hand) != 1:
        return False

    cards_numbers = sorted(get_all_numbers_from_hand(hand), key=lambda element: cards[element])

    cards_values = [cards[x] for x in cards_numbers]

    for i in range(1, len(cards_values)):
        if cards_values[i] != cards_values[i - 1] + 1:
            return False

    return True


def is_n_kind(n, hand):
    return int(n) in get_number_ocurrences_cards(hand).values()


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


hands = [[('J', 'D'), ('10', 'D'), ('K', 'D'), ('Q', 'D'), ('A', 'D')]]

# print(get_number_ocurrences_cards(hands[0]))

print(5 in cards.values())