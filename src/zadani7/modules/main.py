from bank_filter import filter_banks
from explanation import get_explanation
from user_input import get_user_input
from decision_maker import choose_best_bank
from data_loader import load_bank_data


# Modul: main.py
# Úloha: Znalostní systém pro výběr nejlepší banky pro spořicí účet
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 01.12.2024

# Tento modul je hlavní částí programu, která koordinuje všechny moduly.
# Zajišťuje načítání dat, filtraci bank, rozhodování o nejlepší bance a zobrazení výsledků uživateli.
# Používá ostatní moduly k provedení všech kroků procesu a zajišťuje správný běh aplikace.


def main():
    """
        Hlavní funkce programu, která koordinuje všechny kroky: načítání dat, získávání vstupu od uživatele,
        filtrování bank, rozhodování o nejlepší bance a zobrazení výsledků.
        :return: Žádné
        """
    # Načtení dat o bankách
    banks = load_bank_data("../data/banks.json")

    # Získání vstupu od uživatele
    deposit, transactions, investment, city_info = get_user_input()

    # Filtrování bank podle základních podmínek
    eligible_banks = filter_banks(banks, deposit, city_info)

    # Pokud neexistují žádné vhodné banky
    if not eligible_banks:
        print("Neexistují žádné banky, které by vyhovovaly vašim podmínkám.")
        return

    # Výběr nejlepší banky
    best_bank, best_rate, reason = choose_best_bank(eligible_banks, deposit, transactions, investment)

    explanation = get_explanation(best_bank, best_rate, reason, city_info)
    # Zobrazení výsledků
    print("\nNejlepší volba:")
    print(explanation)
    input("EXIT")


if __name__ == "__main__":
    main()
