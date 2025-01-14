# Modul: knowledge_base.py
# Úloha: Einstein's Riddle
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 14.01.2025


"""
@file knowledge_base.py
@brief Provides the foundational data and utility functions for solving Einstein's Riddle.

This module includes:
- Predefined sets of possible attribute values for houses.
- A utility function to generate all permutations of these attributes for use in solving the riddle.

@details The predefined attributes (colors, nationalities, drinks, cigarettes, and pets) represent the constraints
of the riddle. The function `get_all_combinations` generates all possible arrangements of these attributes,
which serve as the basis for finding valid solutions.
"""

from itertools import permutations

# Possible attribute values for houses
colors = ["red", "green", "white", "yellow", "blue"]
nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
drinks = ["milk", "coffee", "tea", "orange juice", "water"]
cigarettes = ["Sparty", "Chesterfield", "Winston", "Lucky Strike", "Parliaments"]
pets = ["dog", "snails", "fox", "horse", "zebra"]


def get_all_combinations():
    """
    @brief Generates all possible permutations of house attributes.

    @details This function creates permutations for each attribute category:
    colors, nationalities, drinks, cigarettes, and pets. These permutations
    represent all potential arrangements of the attributes, which can then
    be filtered based on the riddle's constraints.

    @return A tuple containing lists of permutations for each attribute category:
    (colors_permutations, nationalities_permutations, drinks_permutations,
    cigarettes_permutations, pets_permutations).
    """
    return (
        list(permutations(colors)),
        list(permutations(nationalities)),
        list(permutations(drinks)),
        list(permutations(cigarettes)),
        list(permutations(pets)),
    )
