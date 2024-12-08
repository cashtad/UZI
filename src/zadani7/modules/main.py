from src.zadani7.modules.explanation import get_explanation
from user_input import get_user_input
from bank_filter import filter_banks_by_basic_conditions, filter_banks_by_city
from decision_maker import choose_best_bank
from data_loader import load_bank_data

def main():
    # Načtení dat o bankách
    banks = load_bank_data("data/banks.json")

    # Získání vstupu od uživatele
    deposit, transactions, investment, city_info = get_user_input()

    # Filtrování bank podle základních podmínek
    eligible_banks = filter_banks_by_city(banks, city_info)
    eligible_banks = filter_banks_by_basic_conditions(eligible_banks, deposit)


    # Pokud neexistují žádné vhodné banky
    if not eligible_banks:
        print("Neexistují žádné banky, které by vyhovovaly vašim podmínkám.")
        return

    # Výběr nejlepší banky
    best_bank, best_rate, reason = choose_best_bank(eligible_banks, deposit, transactions, investment)

    explanation = get_explanation(best_bank, best_rate, reason)
    # Zobrazení výsledků
    print("\nNejlepší volba:")
    print(explanation)

if __name__ == "__main__":
    main()
