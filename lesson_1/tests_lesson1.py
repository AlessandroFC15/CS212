import unittest
from lesson_1 import lesson1 as poker

class Test(unittest.TestCase):
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
    flush_1 = [('2', 'D'), ('8', 'D'), ('9', 'D'), ('5', 'D'), ('A', 'D')]
    flush_2 = [('5', 'C'), ('4', 'C'), ('7', 'C'), ('2', 'C'), ('K', 'C')]

    # Straight
    straight = [('5', 'C'), ('6', 'H'), ('7', 'S'), ('8', 'C'), ('9', 'S')]

    # 2-Pair
    two_pair = [('4', 'H'), ('7', 'H'), ('7', 'D'), ('J', 'C'), ('J', 'H')]
    two_pair_2 = [('10', 'H'), ('10', 'C'), ('6', 'S'), ('6', 'C'), ('K', 'H')]

    def test_royal_flush(self):
        self.assertTrue(poker.is_royal_flush(self.royal_flush_hand))
        self.assertFalse(poker.is_royal_flush(self.same_suit_hand))
        self.assertFalse(poker.is_royal_flush(self.straight_flush_hand))

    def test_straight_flush(self):
        self.assertTrue(poker.is_straight_flush(self.straight_flush_hand))
        self.assertTrue(poker.is_straight_flush(self.straight_flush_hand_2))
        self.assertTrue(poker.is_straight_flush(self.royal_flush_hand))
        self.assertFalse(poker.is_straight_flush(self.same_suit_hand))

    def test_4_kind(self):
        self.assertFalse(poker.is_n_kind(4, self.royal_flush_hand))
        self.assertFalse(poker.is_n_kind(4, self.same_suit_hand))
        self.assertFalse(poker.is_n_kind(4, self.straight_flush_hand))
        self.assertTrue(poker.is_n_kind(4, self.four_kind))

    def test_full_house(self):
        self.assertTrue(poker.is_full_house(self.full_house))
        self.assertTrue(poker.is_full_house(self.full_house_2))
        self.assertFalse(poker.is_full_house(self.royal_flush_hand))
        self.assertFalse(poker.is_full_house(self.same_suit_hand))
        self.assertFalse(poker.is_full_house(self.straight_flush_hand))

    def test_flush(self):
        self.assertTrue(poker.is_flush(self.flush))
        self.assertTrue(poker.is_flush(self.royal_flush_hand))
        self.assertTrue(poker.is_flush(self.same_suit_hand))
        self.assertTrue(poker.is_flush(self.straight_flush_hand))
        self.assertTrue(poker.is_flush(self.straight_flush_hand_2))
        self.assertFalse(poker.is_flush(self.four_kind))
        self.assertFalse(poker.is_flush(self.full_house))
        self.assertFalse(poker.is_flush(self.full_house_2))

    def test_straight(self):
        self.assertTrue(poker.is_straight(self.straight_flush_hand))
        self.assertTrue(poker.is_straight(self.straight_flush_hand_2))
        self.assertFalse(poker.is_straight(self.four_kind))
        self.assertFalse(poker.is_straight(self.full_house))
        self.assertFalse(poker.is_straight(self.full_house_2))
        self.assertFalse(poker.is_straight(self.flush))

    def test_two_pair(self):
        self.assertTrue(poker.is_two_pair(self.two_pair))
        self.assertFalse(poker.is_two_pair(self.royal_flush_hand))
        self.assertFalse(poker.is_two_pair(self.same_suit_hand))
        self.assertFalse(poker.is_two_pair(self.straight_flush_hand))
        self.assertFalse(poker.is_two_pair(self.straight_flush_hand_2))
        self.assertFalse(poker.is_two_pair(self.four_kind))

    # Testing the computing of ranks
    def test_flush_rank(self):
        self.assertEqual(poker.compute_rank(self.flush), (6, 14, 11, 10, 8, 5))
        self.assertEqual(poker.compute_rank(self.flush_1), (6, 14, 9, 8, 5, 2))
        self.assertEqual(poker.compute_rank(self.flush_2), (6, 13, 7, 5, 4, 2))

    def test_straight_rank(self):
        self.assertEqual(poker.compute_rank(self.straight), (5, 9))

    def test_two_pair_rank(self):
        self.assertEqual(poker.compute_rank(self.two_pair), (3, 11, 7, 4))
        self.assertEqual(poker.compute_rank(self.two_pair_2), (3, 10, 6, 13))

    # Test for real
    def test_poker(self):
        self.assertEqual(poker.poker([self.flush, self.flush_1, self.flush_2]), self.flush)


if __name__ == '__main__':
    unittest.main()