# Lesson 1 | About the Class

# || Comments ||
# I feel my solution was very similar to the proposed solution in class. What I was trying to accomplish was pretty much
# the same thing the teacher tried, I was simply not aware of the list generation method and I feel I sort of over
# complicated a lit bit with the map and lambda stuff. It is what it is. I've learned now.

def ss(lst):
    listSquaredNumbers = list(map(lambda x: x * x, lst))

    return sum(listSquaredNumbers)

# print (ss([1, 2, 3]))

# Lesson 1 | Poker hand
def poker(hands):
    """Return the best hand: poker([hand, ...]) => hand"""

    for hand in hands:

        if isRoyalFlush(hand):
            print ("Royal flush, brother!")
        else:
            print ("Boooooo")

    # 1st step => Calculate rankings for each hand

    # 2nd step => Return the highest one


def getAllNumbersFromHand(hand):
    return [x[0] for x in hand]

def getAllSuitsFromHand(hand):
    return [x[1] for x in hand]

def getNumberDifferentSuits(hand):
    return len(set(getAllSuitsFromHand(hand)))

hands = [[('10', 'D'), ('J', 'D'), ('Q', 'D'), ('K', 'D'), ('A', 'D')]]

print(getNumberDifferentSuits(hands[0]))

# poker(hands)