# knowledge_base.py

from itertools import permutations

# Возможные значения для характеристик
colors = ["red", "green", "white", "yellow", "blue"]
nationalities = ["Englishman", "Spaniard", "Ukrainian", "Norwegian", "Japanese"]
drinks = ["milk", "coffee", "tea", "orange juice", "water"]
cigarettes = ["Sparty", "Chesterfield", "Winston", "Lucky Strike", "Parliaments"]
pets = ["dog", "snails", "fox", "horse", "zebra"]

def get_all_combinations():
    """Генерирует все возможные комбинации характеристик"""
    return (
        list(permutations(colors)),
        list(permutations(nationalities)),
        list(permutations(drinks)),
        list(permutations(cigarettes)),
        list(permutations(pets)),
    )
