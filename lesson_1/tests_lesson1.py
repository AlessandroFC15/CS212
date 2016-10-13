import unittest
from lesson_1 import lesson1 as poker

class Test(unittest.TestCase):
    royal_flush_hand = [('J', 'D'), ('10', 'D'), ('Q', 'D'), ('K', 'D'), ('A', 'D')]
    same_suit_hand = [('2', 'D'), ('5', 'D'), ('Q', 'D'), ('7', 'D'), ('3', 'D')]

    # Straight flush
    straight_flush_hand = [('5', 'S'), ('6', 'S'), ('7', 'S'), ('8', 'S'), ('9', 'S')]
    straight_flush_hand_2 = [('6', 'C'), ('5', 'C'), ('4', 'C'), ('3', 'C'), ('2', 'C')]
    straight_flush_hand_3 = [('J', 'C'), ('10', 'C'), ('9', 'C'), ('8', 'C'), ('7', 'C')]

    # Four of a kind
    four_kind = [('6', 'D'), ('6', 'C'), ('6', 'S'), ('6', 'C'), ('2', 'H')]
    four_kind_2 = [('A', 'C'), ('A', 'S'), ('A', 'H'), ('A', 'D'), ('Q', 'H')]

    # Full-house
    full_house = [('J', 'D'), ('J', 'C'), ('J', 'S'), ('2', 'C'), ('2', 'H')]
    full_house_2 = [('5', 'D'), ('9', 'C'), ('5', 'S'), ('9', 'C'), ('9', 'H')]
    full_house_3 = [('8', 'S'), ('8', 'H'), ('8', 'D'), ('K', 'C'), ('K', 'S')]

    # Flush
    flush = [('5', 'H'), ('8', 'H'), ('10', 'H'), ('J', 'H'), ('A', 'H')]
    flush_1 = [('2', 'D'), ('8', 'D'), ('9', 'D'), ('5', 'D'), ('A', 'D')]
    flush_2 = [('5', 'C'), ('4', 'C'), ('7', 'C'), ('2', 'C'), ('K', 'C')]
    flush_3 = [('10', 'D'), ('8', 'D'), ('7', 'D'), ('5', 'D'), ('3', 'D')]

    # Straight
    straight = [('5', 'C'), ('6', 'H'), ('7', 'S'), ('8', 'C'), ('9', 'S')]
    straight_2 = [('J', 'C'), ('10', 'S'), ('9', 'D'), ('8', 'C'), ('7', 'C')]

    # Three of a king
    three_kind = [('7, H'), ('7', 'D'), ('7', 'C'), ('5', 'C'), ('2', 'C')]

    # 2-Pair
    two_pair = [('4', 'H'), ('7', 'H'), ('7', 'D'), ('J', 'C'), ('J', 'H')]
    two_pair_2 = [('10', 'H'), ('10', 'C'), ('6', 'S'), ('6', 'C'), ('K', 'H')]
    two_pair_3 = [('J', 'D'), ('J', 'C'), ('3', 'S'), ('3', 'H'), ('K', 'H')]

    # Pair of two
    pair_two = [('2', 'H'), ('2', 'S'), ('J', 'D'), ('6', 'H'), ('3', 'C')]

    def test_royal_flush(self):
        self.assertTrue(poker.is_royal_flush(self.royal_flush_hand))
        self.assertFalse(poker.is_royal_flush(self.same_suit_hand))
        self.assertFalse(poker.is_royal_flush(self.straight_flush_hand))

    def test_straight_flush(self):
        self.assertTrue(poker.is_straight(self.straight_flush_hand) and poker.is_flush(self.straight_flush_hand))
        self.assertTrue(poker.is_straight(self.straight_flush_hand_2) and poker.is_flush(self.straight_flush_hand_2))
        self.assertTrue(poker.is_straight(self.royal_flush_hand) and poker.is_flush(self.royal_flush_hand))
        self.assertFalse(poker.is_straight(self.same_suit_hand) and poker.is_flush(self.same_suit_hand))

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
        self.assertEqual(poker.compute_rank(self.flush_3), (6, 10, 8, 7, 5, 3))

    def test_straight_rank(self):
        self.assertEqual(poker.compute_rank(self.straight), (5, 9))
        self.assertEqual(poker.compute_rank(self.straight_2), (5, 11))

    def test_two_pair_rank(self):
        self.assertEqual(poker.compute_rank(self.two_pair), (3, 11, 7, 4))
        self.assertEqual(poker.compute_rank(self.two_pair_2), (3, 10, 6, 13))
        self.assertEqual(poker.compute_rank(self.two_pair_3), (3, 11, 3, 13))

    def test_straight_flush_rank(self):
        self.assertEqual(poker.compute_rank(self.straight_flush_hand), (9, 9))
        self.assertEqual(poker.compute_rank(self.straight_flush_hand_2), (9, 6))
        self.assertEqual(poker.compute_rank(self.straight_flush_hand_3), (9, 11))

    def test_four_kind_rank(self):
        self.assertEqual(poker.compute_rank(self.four_kind), (8, 6, 2))
        self.assertEqual(poker.compute_rank(self.four_kind_2), (8, 14, 12))

    def test_full_house_rank(self):
        self.assertEqual(poker.compute_rank(self.full_house_3), (7, 8, 13))
        self.assertEqual(poker.compute_rank(self.full_house_2), (7, 9, 5))
        self.assertEqual(poker.compute_rank(self.full_house), (7, 11, 2))

    def test_three_kind_rank(self):
        self.assertEqual(poker.compute_rank(self.three_kind), (4, 7, 5, 2))

    def test_pair_two_rank(self):
        self.assertEqual(poker.compute_rank(self.pair_two), (2, 2, 11, 6, 3))

    # Test for real
    def test_poker(self):
        self.assertEqual(poker.poker([self.flush, self.flush_1, self.flush_2]), self.flush)


if __name__ == '__main__':
    unittest.main()