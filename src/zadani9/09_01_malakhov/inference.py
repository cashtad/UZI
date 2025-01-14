# inference.py

def is_valid_solution(houses):
    """Проверка выполнения всех правил"""

    #13. The green house is immediately to the right of the white house
    try:
        assert any(
            houses[i]["color"] == "white" and houses[i+1]["color"] == "green"
            for i in range(len(houses) - 1)
        )
    except AssertionError:
        return "color"

    # 3. The Norwegians live in the first house on the left
    try:
        assert houses[0]["nationality"] == "Norwegian"
    except AssertionError:
        return "nationalities"

    # 1. The English live in the red house
    try:
        assert any(house["nationality"] == "Englishman" and house["color"] == "red" for house in houses)
    except AssertionError:
        return "nationalities"

    # 6. The Norwegians live in the blue house
    try:
        assert any(house["nationality"] == "Norwegian" and house["color"] == "blue" for house in houses)
    except AssertionError:
        return "nationalities"

    # 14. In the middle house, they drink milk
    try:
        assert houses[2]["drink"] == "milk"
    except AssertionError:
        return "drinks"

    # 12. In the green house, they drink coffee
    try:
        assert any(
            houses[i]["color"] == "green" and houses[i]["drink"] == "coffee"
            for i in range(len(houses))
        )
    except AssertionError:
        return "drinks"

    # 9. The Ukrainians drink tea
    try:
        assert any(
            house["nationality"] == "Ukrainian" and house["drink"] == "tea" for house in houses
        )
    except AssertionError:
        return "drinks"

    # 4. The residents of the yellow house smoke Sparty cigarettes
    try:
        assert any(house["color"] == "yellow" and house["cigarette"] == "Sparty" for house in houses)
    except AssertionError:
        return "cigarettes"

    # 8. The Lucky Strike smoker drinks orange juice
    try:
        assert any(house["drink"] == "orange juice" and house["cigarette"] == "Lucky Strike" for house in houses)
    except AssertionError:
        return "cigarettes"

    # 10. The Japanese smoke Parliaments cigarettes
    try:
        assert any(house["nationality"] == "Japanese" and house["cigarette"] == "Parliaments" for house in houses)
    except AssertionError:
        return "cigarettes"

    # 2. The Spaniards have a dog
    try:
        assert any(house["nationality"] == "Spaniard" and house["pet"] == "dog" for house in houses)
    except AssertionError:
        return "pets"

    # 7. The Winston smoker keeps snails
    try:
        assert any(house["cigarette"] == "Winston" and house["pet"] == "snails" for house in houses)
    except AssertionError:
        return "pets"

    # 11. In the house next to the one with a horse, Sparty cigarettes are smoked
    try:
        assert any(
            (i == 0 and houses[i]["pet"] == "horse" and
            (houses[i + 1]["cigarette"] == "Sparty")) or
            (0 < i < len(houses) - 1 and houses[i]["pet"] == "horse" and
             ("Sparty" in houses[i-1]["cigarette"], houses[i+1]["cigarette"]) or
             (i == len(houses) - 1 and houses[i]["pet"] == "horse") and
             houses[i-1]["cigarette"] == "Sparty")
            for i in range(0, len(houses))
        )
    except AssertionError:
        return "pets"

    # 5. The man who smokes Chesterfields lives next to the house of the family that has a fox
    try:
        assert any(
            (i == 0 and houses[i]["cigarette"] == "Chesterfield" and
            (houses[i + 1]["pet"] == "fox")) or
            (0 < i < len(houses) - 1 and houses[i]["cigarette"] == "Chesterfield" and
             ("fox" in houses[i-1]["pet"], houses[i+1]["pet"])) or
             (i == len(houses) - 1 and houses[i]["cigarette"] == "Chesterfield" and
             houses[i-1]["pet"] == "fox")
            for i in range(0, len(houses))
        )
    except AssertionError:
        return "pets"

    return True


def solve_puzzle(combinations):
    """Поиск решения методом перебора"""
    colors_perm, nationalities_perm, drinks_perm, cigarettes_perm, pets_perm = combinations
    solved = []
    current_skip = ""
    for perm_colors in colors_perm:
        if current_skip == "color":
            current_skip = ""
        for perm_nationalities in nationalities_perm:
            if (current_skip != "nationalities" and current_skip != "drinks" and current_skip != "cigarettes" and current_skip != "pets") and current_skip != "":
                break
            if current_skip == "nationalities":
                current_skip = ""

            for perm_drinks in drinks_perm:
                if (current_skip != "drinks" and current_skip != "cigarettes" and current_skip != "pets") and current_skip != "":
                    break
                if current_skip == "drinks":
                    current_skip = ""

                for perm_cigarettes in cigarettes_perm:
                    if (current_skip != "cigarettes" and current_skip != "pets") and current_skip != "":
                        break
                    if current_skip == "cigarettes":
                        current_skip = ""

                    for perm_pets in pets_perm:
                        if current_skip != "pets" and current_skip != "":
                            break
                        if current_skip == "pets":
                            current_skip = ""
                        houses = [
                            {
                                "color": perm_colors[i],
                                "nationality": perm_nationalities[i],
                                "drink": perm_drinks[i],
                                "cigarette": perm_cigarettes[i],
                                "pet": perm_pets[i],
                            }
                            for i in range(5)
                        ]
                        if is_valid_solution(houses) == True:
                            solved.append(houses)
                        else:
                            current_skip = is_valid_solution(houses)
    return solved
