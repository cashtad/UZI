# main.py

import knowledge_base
import inference
import explanation

def main():
    """Основная функция запуска программы"""
    explanation.print_intro()
    combinations = knowledge_base.get_all_combinations()
    solutions = inference.solve_puzzle(combinations)
    explanation.explain_solutions(solutions)


if __name__ == "__main__":
    main()
