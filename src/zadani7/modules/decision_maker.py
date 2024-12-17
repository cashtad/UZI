from bonus_checker import check_bonus_conditions


# Modul: decision_maker.py
# Úloha: Znalostní systém pro výběr nejlepší banky pro spořicí účet
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 01.12.2024
# Tento modul obsahuje funkci pro rozhodování o nejlepší bance na základě zadaných parametrů.

def choose_best_bank(banks, deposit, transactions, investment):
    """
       Funkce vybírá nejlepší banku na základě úrokové sazby a podmínek pro bonusovou úrokovou sazbu.
       :param banks: Seznam bank
       :param deposit: Částka vkladu uživatele
       :param transactions: Počet transakcí uživatele
       :param investment: Výše měsíčního investování uživatele
       :return: Nejlepší banka, její úroková sazba a důvod výběru
       """
    best_bank = None
    best_rate = 0
    reason = ""

    for bank in banks:
        basic_rate = float(bank["interest_rate_basic"].replace(",", "."))
        bonus_rate = float(bank["interest_rate_bonus"].replace(",", "."))
        if check_bonus_conditions(bank, deposit, transactions, investment):
            rate = bonus_rate
            reason_test = "Bonusová sazba je dostupná díky splnění všech podmínek."
        else:
            rate = basic_rate
            reason_test = "Bonusová sazba není dostupná, uvažuje se základní sazba."

        if rate > best_rate:
            best_bank = bank
            best_rate = rate
            reason = reason_test

    return best_bank, best_rate, reason
