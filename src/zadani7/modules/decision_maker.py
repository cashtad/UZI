from src.zadani7.modules.bonus_checker import check_bonus_conditions


def choose_best_bank(banks, deposit, transactions, investment):
    best_bank = None
    best_rate = 0
    reason = ""

    for bank in banks:
        basic_rate = float(bank["interest_rate_basic"].replace(",", "."))
        bonus_rate = float(bank["interest_rate_bonus"].replace(",", "."))
        reason_test = ""
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
