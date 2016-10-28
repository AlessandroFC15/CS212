import itertools

def populate_data_houses(dictionary, attribute, houses):
    for item in dictionary:
        houses[item][attribute] = dictionary[item]

def is_immediately_to_right_of(house_1, house_2):
    """Check if a house is immediately to the the right of some other house based on their numbers.

        It should be read as 'Is house_1 located immediately to the right of house_2?'

    @ Args:
        house_1: House that you want to check if it is to the right of house_2
        house_2: House that is the reference to check if house_1 is to the right if this house
    """
    return house_1 - 1 == house_2

def is_next_to(house_1, house_2):
    """Check if a house is next to some other house based on their numbers.

        It should be read as 'Is house_1 located next to house_2?'
        """
    return house_1 in [house_2 + 1, house_2 - 1]

def get_full_solution_zebra_puzzle():
    """Returns a dictionary mapping the house numbers to its respective houses

    Each house will contains the following values: color, nation of its owner, pet of owner, what the owner drinks
    and what the owner smokes.
    """

    houses_numbers = [1, 2, 3, 4, 5]
    houses = {item: {} for item in houses_numbers}
    orderings = list(itertools.permutations(houses_numbers))

    for (red, green, yellow, blue, ivory) in orderings:
        if not is_immediately_to_right_of(green, ivory):
            continue

        for (england, spain, ukraine, norway, japan) in orderings:
            if england != red or norway != 1 or not is_next_to(norway, blue):
                continue

            for (dog, snails, fox, horse, zebra) in orderings:
                if spain != dog:
                    continue

                for (milk, coffee, tea, orange_juice, water) in orderings:
                    if coffee != green or ukraine != tea or milk != 3:
                        continue

                    for (old_gold, kolls, chesterfields, lucky_striker, parliaments) in orderings:
                        if old_gold != snails or kolls != yellow or lucky_striker != orange_juice or \
                            japan != parliaments or not is_next_to(chesterfields, fox) or not is_next_to(kolls, horse):
                            continue

                        # Populating houses
                        colors = {red: 'RED', green: 'GREEN', yellow: 'YELLOW', blue: 'BLUE', ivory: 'IVORY'}
                        populate_data_houses(colors, 'color', houses)

                        nations = {england: 'ENGLAND', spain: 'SPAIN', ukraine: 'UKRAINE', norway: 'NORWAY',
                                   japan: 'JAPAN'}
                        populate_data_houses(nations, 'nation', houses)

                        pets = {dog: 'DOG', snails: 'SNAILS', fox: 'FOX', horse: 'HORSE', zebra: 'ZEBRA'}
                        populate_data_houses(pets, 'pet', houses)

                        drinks = {milk: 'MILK', coffee: 'COFFEE', tea: 'TEA', orange_juice: 'ORANGE JUICE',
                                  water: 'WATER'}
                        populate_data_houses(drinks, 'drinks', houses)

                        smokes = {old_gold: 'OLD GOLD', kolls: 'KOLLS', chesterfields: 'chesterfields',
                                  lucky_striker: 'lucky_striker', parliaments: 'parliaments'}
                        populate_data_houses(smokes, 'smokes', houses)

                        for house_number in houses:
                            print('HOUSE NUMBER %d' % house_number)
                            print(houses[house_number])
                            print('-----------')

                        return houses

def get_zebra_and_water_house_numbers():
    """ Returns a dictionary like the following

        {'WATER': water house number goes here, 'ZEBRA': zebra house_number goes here}
    """
    solution = get_full_solution_zebra_puzzle()
    zebra = None
    water = None

    for house_number, data in solution.items():
        if data['pet'] == 'ZEBRA':
            zebra = house_number

        if data['drinks'] == 'WATER':
            water = house_number

    return {'WATER': water, 'ZEBRA': zebra}

print(get_zebra_and_water_house_numbers())