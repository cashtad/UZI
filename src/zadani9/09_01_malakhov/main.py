# Modul: main.py
# Úloha: Einstein's Riddle
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 14.01.2025


"""
@file main.py
@brief Entry point for solving Einstein's Riddle.

@details This script integrates all components of the program. It:
- Introduces the puzzle to the user.
- Generates all possible combinations of house attributes.
- Finds solutions to the puzzle using the inference module.
- Explains the solutions to the user.

@note Ensure all modules (knowledge_base, inference, explanation) are in the same directory
or properly installed in the Python environment.
"""

import knowledge_base
import inference
import explanation


def main():
    """
    @brief Main function to execute the program.

    @details The function:
    1. Prints an introduction to the puzzle.
    2. Generates all permutations of attributes from the knowledge base.
    3. Finds solutions using the inference module.
    4. Explains the solutions to the user in a readable format.
    """
    explanation.print_intro()
    combinations = knowledge_base.get_all_combinations()
    solutions = inference.solve_puzzle(combinations)
    explanation.explain_solutions(solutions)


if __name__ == "__main__":
    main()
