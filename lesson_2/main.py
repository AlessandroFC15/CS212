import itertools

def populate_data_houses(dictionary, attribute, houses):
    for item in dictionary:
        houses[item][attribute] = dictionary[item]

def get_solution_zebra_puzzle():
    houses_numbers = [1, 2, 3, 4, 5]
    houses = {item: {} for item in houses_numbers}
    orderings = list(itertools.permutations(houses_numbers))

    for (red, green, yellow, blue, ivory) in orderings:
        if green - 1 != ivory:  # The green house is immediately to the right of the ivory house.
            continue

        for (england, spain, ukraine, norway, japan) in orderings:
            if england != red or norway != 1 or not (norway in [blue + 1, blue - 1]):
                continue

            for (dog, snails, fox, horse, zebra) in orderings:
                if spain != dog:
                    continue

                for (milk, coffee, tea, orange_juice, water) in orderings:
                    if coffee != green or ukraine != tea or milk != 3:
                        continue

                    for (old_gold, kolls, chesterfields, lucky_striker, parliaments) in orderings:
                        if old_gold != snails or kolls != yellow or lucky_striker != orange_juice or japan != parliaments:
                            continue

                        # The man who smokes Chesterfields lives in the house next to the man with the fox.
                        if not (chesterfields in [fox + 1, fox - 1]):
                            continue

                        # Kools are smoked in the house next to the house where the horse is kept.
                        if not (kolls in [horse + 1, horse - 1]):
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

                        # for house_number in houses:
                        #     print('HOUSE NUMBER %d' % house_number)
                        #     print(houses[house_number])
                        #     print('-----------')

                        return houses