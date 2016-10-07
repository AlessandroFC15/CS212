import unittest
from lesson_1 import lesson1 as poker

class Test(unittest.TestCase):
    royal_flush_hand = [('J', 'D'), ('10', 'D'), ('Q', 'D'), ('K', 'D'), ('A', 'D')]
    same_suit_hand = [('2', 'D'), ('5', 'D'), ('Q', 'D'), ('7', 'D'), ('3', 'D')]
    straight_flush_hand = [('5', 'S'), ('6', 'S'), ('7', 'S'), ('8', 'S'), ('9', 'S')]
    straight_flush_hand_2 = [('6', 'C'), ('5', 'C'), ('4', 'C'), ('3', 'C'), ('2', 'C')]
    four_kind = [('6', 'D'), ('6', 'C'), ('6', 'S'), ('6', 'C'), ('2', 'H')]

    def test_royal_flush(self):
        self.assertTrue(poker.is_royal_flush(self.royal_flush_hand))
        self.assertFalse(poker.is_royal_flush(self.same_suit_hand))
        self.assertFalse(poker.is_royal_flush(self.straight_flush_hand))

    def test_straight_flush(self):
        self.assertTrue(poker.is_straight_flush(self.straight_flush_hand, poker.cards))
        self.assertTrue(poker.is_straight_flush(self.straight_flush_hand_2, poker.cards))
        self.assertTrue(poker.is_straight_flush(self.royal_flush_hand, poker.cards))
        self.assertFalse(poker.is_straight_flush(self.same_suit_hand, poker.cards))

    def test_4_kind(self):
        self.assertFalse(poker.is_n_kind(4, self.royal_flush_hand))
        self.assertFalse(poker.is_n_kind(4, self.same_suit_hand))
        self.assertFalse(poker.is_n_kind(4, self.straight_flush_hand))
        self.assertTrue(poker.is_n_kind(4, self.four_kind))

if __name__ == '__main__':
    unittest.main()