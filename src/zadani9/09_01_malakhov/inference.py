# Modul: inference.py
# Úloha: Einstein's Riddle
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 14.01.2025


"""
@file inference.py
@brief Contains the core logic for validating and solving Einstein's Riddle.

This module includes:
- A function to check if a given house arrangement satisfies all constraints of the riddle.
- A function to find all valid solutions using a brute-force approach.

@details The validation function ensures compliance with all clues from the riddle, such as the positions of houses,
occupants, pets, drinks, and cigarettes. The solving function iterates through all possible permutations of attributes,
filtering out invalid combinations to find solutions.
"""


def is_valid_solution(houses):
    """
    @brief Validates a house arrangement against the rules of Einstein's Riddle.

    @details This function checks whether a given configuration of houses satisfies all the riddle's constraints.
    Each rule corresponds to a specific clue from the riddle, and assertions are used to validate the rules.

    @param houses A list of dictionaries, where each dictionary represents a house with its attributes:
    color, nationality, drink, cigarette, and pet.

    @return True if the arrangement satisfies all rules; otherwise, returns a string indicating
    the category of the failed rule (e.g., "color", "nationalities", "drinks", "cigarettes", or "pets").
    """
    # 13. The green house is immediately to the right of the white house
    try:
        assert any(
            houses[i]["color"] == "white" and houses[i + 1]["color"] == "green"
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
             ("Sparty" in houses[i - 1]["cigarette"], houses[i + 1]["cigarette"]) or
             (i == len(houses) - 1 and houses[i]["pet"] == "horse") and
             houses[i - 1]["cigarette"] == "Sparty")
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
             ("fox" in houses[i - 1]["pet"], houses[i + 1]["pet"])) or
            (i == len(houses) - 1 and houses[i]["cigarette"] == "Chesterfield" and
             houses[i - 1]["pet"] == "fox")
            for i in range(0, len(houses))
        )
    except AssertionError:
        return "pets"

    return True


def solve_puzzle(combinations):
    """
    @brief Finds solutions to Einstein's Riddle using brute force.

    @details This function iterates over all permutations of house attributes, validating each arrangement
    against the riddle's rules using the `is_valid_solution` function. Valid configurations are collected and returned.

    @param combinations A tuple of permutations for each attribute category:
    (colors_permutations, nationalities_permutations, drinks_permutations,
    cigarettes_permutations, pets_permutations).

    @return A list of valid house arrangements that satisfy all constraints.
    Each arrangement is represented as a list of dictionaries, where each dictionary describes a house.
    """
    colors_perm, nationalities_perm, drinks_perm, cigarettes_perm, pets_perm = combinations
    solved = []
    current_skip = ""

    for perm_colors in colors_perm:
        if current_skip == "color":
            current_skip = ""
        for perm_nationalities in nationalities_perm:
            if (
                    current_skip not in ["", "nationalities", "drinks", "cigarettes", "pets"]
            ):
                break
            if current_skip == "nationalities":
                current_skip = ""

            for perm_drinks in drinks_perm:
                if current_skip not in ["", "drinks", "cigarettes", "pets"]:
                    break
                if current_skip == "drinks":
                    current_skip = ""

                for perm_cigarettes in cigarettes_perm:
                    if current_skip not in ["", "cigarettes", "pets"]:
                        break
                    if current_skip == "cigarettes":
                        current_skip = ""

                    for perm_pets in pets_perm:
                        if current_skip != "" and current_skip != "pets":
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
                        result = is_valid_solution(houses)
                        if result is True:
                            solved.append(houses)
                        else:
                            current_skip = result
    return solved
