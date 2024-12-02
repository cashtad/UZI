from src.zadani7.modules.explanation import get_explanation
from user_input import get_user_input
from bank_filter import filter_banks_by_basic_conditions
from decision_maker import choose_best_bank
from data_loader import load_bank_data

def main():
    # Загружаем данные о банках
    banks = load_bank_data("data/banks.json")

    # Получаем ввод от пользователя
    deposit, transactions, investment = get_user_input()

    # Фильтруем банки по базовым условиям
    eligible_banks = filter_banks_by_basic_conditions(banks, deposit)

    # Если нет подходящих банков
    if not eligible_banks:
        print("Нет банков, подходящих для ваших условий.")
        return

    # Выбираем лучший банк
    best_bank, best_rate, reason = choose_best_bank(eligible_banks, deposit, transactions, investment)

    explanation = get_explanation(best_bank, best_rate, reason)
    # Выводим результаты
    print("\nЛучший выбор:")
    print(explanation)

if __name__ == "__main__":
    main()
