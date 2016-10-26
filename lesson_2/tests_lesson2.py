import unittest
from lesson_2 import main

class TestLesson2(unittest.TestCase):
    houses = main.get_full_solution_zebra_puzzle()

    def test_rules(self):
        self.assertTrue(self.test_rule_1())
        self.assertTrue(self.test_rule_2())
        self.assertTrue(self.test_rule_3())
        self.assertTrue(self.test_rule_4())
        self.assertTrue(self.test_rule_5())
        self.assertTrue(self.test_rule_6())
        self.assertTrue(self.test_rule_7())
        self.assertTrue(self.test_rule_8())
        self.assertTrue(self.test_rule_9())
        self.assertTrue(self.test_rule_10())
        self.assertTrue(self.test_rule_11())
        self.assertTrue(self.test_rule_12())
        self.assertTrue(self.test_rule_13())
        self.assertTrue(self.test_rule_14())

    # 1. The Englishman lives in the red house.
    def test_rule_1(self):
        for house_number, data in self.houses.items():
            if data['color'] == 'RED' and data['nation'] == 'ENGLAND':
                return True

        return False

    # 2. The Spaniard owns the dog.
    def test_rule_2(self):
        for house_number, data in self.houses.items():
            if data['nation'] == 'SPAIN' and data['pet'] == 'DOG':
                return True

        return False

    # 3. Coffee is drunk in the green house.
    def test_rule_3(self):
        for house_number, data in self.houses.items():
            if data['drinks'] == 'COFFEE' and data['color'] == 'GREEN':
                return True

        return False

    # 4. The Ukrainian drinks tea.
    def test_rule_4(self):
        for house_number, data in self.houses.items():
            if data['nation'] == 'UKRAINE' and data['drinks'] == 'TEA':
                return True

        return False

    # 5. The green house is immediately to the right of the ivory house.
    def test_rule_5(self):
        green_house_number = 0
        ivory_house_number = 0

        for house_number, data in self.houses.items():
            if data['color'] == 'GREEN':
                green_house_number = house_number
            elif data['color'] == 'IVORY':
                ivory_house_number = house_number

        return green_house_number == ivory_house_number + 1

    # 6. The Old Gold smoker owns snails.
    def test_rule_6(self):
        for house_number, data in self.houses.items():
            if data['smokes'] == 'OLD GOLD' and data['pet'] == 'SNAILS':
                return True

        return False

    # 7. Kools are smoked in the yellow house.
    def test_rule_7(self):
        for house_number, data in self.houses.items():
            if data['smokes'] == 'KOLLS' and data['color'] == 'YELLOW':
                return True

        return False

    # 8. Milk is drunk in the middle house.
    def test_rule_8(self):
        for house_number, data in self.houses.items():
            if data['drinks'] == 'MILK' and house_number == 3:
                return True

        return False

    # 9. The Norwegian lives in the first house.
    def test_rule_9(self):
        for house_number, data in self.houses.items():
            if data['nation'] == 'NORWAY' and house_number == 1:
                return True

        return False

    # 10. The man who smokes Chesterfields lives in the house next to the man with the fox.
    def test_rule_10(self):
        house_number_chesterfields = 0
        house_number_fox = 0

        for house_number, data in self.houses.items():
            if data['smokes'] == 'chesterfields':
                house_number_chesterfields = house_number
            elif data['pet'] == 'FOX':
                house_number_fox = house_number

        return house_number_chesterfields in [house_number_fox + 1, house_number_fox - 1]

    # 11. Kools are smoked in the house next to the house where the horse is kept.
    def test_rule_11(self):
        house_number_kools = 0
        house_number_horse = 0

        for house_number, data in self.houses.items():
            if data['smokes'] == 'KOLLS':
                house_number_kools = house_number

            if data['pet'] == 'HORSE':
                house_number_horse = house_number

        return house_number_kools in [house_number_horse + 1, house_number_horse - 1]

    # 12. The Lucky Strike smoker drinks orange juice.
    def test_rule_12(self):
        for house_number, data in self.houses.items():
            if data['smokes'] == 'lucky_striker' and data['drinks'] == 'ORANGE JUICE':
                return True

        return False

    # 13. The Japanese smokes Parliaments.
    def test_rule_13(self):
        for house_number, data in self.houses.items():
            if data['smokes'] == 'parliaments' and data['nation'] == 'JAPAN':
                return True

        return False

    # 14. The Norwegian lives next to the blue house.
    def test_rule_14(self):
        house_number_norway = 0
        house_number_blue = 0

        for house_number, data in self.houses.items():
            if data['nation'] == 'NORWAY':
                house_number_norway = house_number
            elif data['color'] == 'BLUE':
                house_number_blue = house_number

        return house_number_norway in [house_number_blue + 1, house_number_blue - 1]

if __name__ == '__main__':
    unittest.main()