# explanation.py

from prettytable import PrettyTable


def print_intro():
    intro = """Welcome to the Einstein's Riddle!
The goal of this logic puzzle is to determine the layout of five houses in a row, each with unique attributes
associated with their occupant's nationality, house color, drink, pet, and cigarette brand.

Here is what we know:

1. There are five houses in a row, each painted a different color.
2. In each house lives a person of a different nationality.
3. Each person drinks a unique type of beverage, keeps a unique type of pet, and smokes a unique brand of cigarettes.

Based on these hints, can you figure out:
   - Which house belongs to which nationality?
   - What each person drinks, smokes, and keeps as a pet?

Here are the clues:

1. The English live in the red house
2. The Spaniards have a dog
3. The Norwegians live in the first house on the left
4. The residents of the yellow house smoke Sparty cigarettes
5. The man who smokes Chesterfields lives next to the house of the family that has a fox
6. The Norwegians live in the blue house
7. The Winston smoker keeps snails
8. The Lucky Strike smoker drinks orange juice
9. The Ukrainians drink tea
10. The Japanese smoke Parliaments cigarettes
11. In the house next to the one with a horse, Sparty cigarettes are smoked
12. In the green house, they drink coffee
13. The green house is immediately to the right of the white house
14. In the middle house, they drink milk

The objective is to use these constraints to solve the riddle:

"Who owns the zebra?"
"Who drinks the water?"
"""
    print(intro)


def explain_solutions(solutions):
    """Формирует вывод результатов в формате таблиц."""
    result = []
    count = 0

    if len(solutions) == 0:
        result.append("No solution found.")
        return "\n".join(result)

    for solution in solutions:
        count += 1
        result.append(f"Solution: {count}\n")

        # Подготовка таблицы для вывода
        table = PrettyTable()
        table.field_names = ["House", "Color", "Nationality", "Drink", "Cigarette", "Pet"]

        # Заполнение таблицы данными из решения
        for i, house in enumerate(solution, start=1):
            table.add_row([
                i,
                house.get("color", "-"),
                house.get("nationality", "-"),
                house.get("drink", "-"),
                house.get("cigarette", "-"),
                house.get("pet", "-")
            ])

        result.append(table.get_string())

        # Поиск домов с зеброй и водой
        zebra_house = next(i + 1 for i, house in enumerate(solution) if house["pet"] == "zebra")
        water_house = next(i + 1 for i, house in enumerate(solution) if house["drink"] == "water")
        result.append(f"\nThe zebra lives in house {zebra_house}.")
        result.append(f"The house with water is number {water_house}.\n")


    print("\n".join(result))
