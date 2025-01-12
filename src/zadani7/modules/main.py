import bank_filter
import explanation
import output_utils
import user_input
import decision_maker
import data_loader


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
    while True:
        output_utils.print_dividing_line()

        # Načtení dat o bankách
        banks = data_loader.load_bank_data("../data/banks.json")

        # Získání vstupu od uživatele
        deposit, transactions, investment, city_info = user_input.get_complete_user_input()

        # Filtrování bank podle základních podmínek
        eligible_banks = bank_filter.filter_banks(banks, deposit, city_info)

        # Výběr nejlepší banky
        best_bank, best_rate, reason = decision_maker.choose_best_bank(eligible_banks, deposit, transactions, investment)

        explanation_text = explanation.get_explanation(best_bank, best_rate, reason, city_info)

        # Zobrazení výsledků
        output_utils.print_result(explanation_text)

        command = user_input.get_start_again_input()
        if command.lower() == "exit":
            break


if __name__ == "__main__":
    main()
