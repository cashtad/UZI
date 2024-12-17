# Modul: bonus_checker.py
# Úloha: Znalostní systém pro výběr nejlepší banky pro spořicí účet
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 01.12.2024

# Tento modul obsahuje funkci pro kontrolu, zda banka splňuje podmínky pro získání bonusové úrokové sazby.


def check_bonus_conditions(bank, deposit, transactions, investment):
    """
        Funkce kontroluje podmínky pro bonusovou úrokovou sazbu.
        :param bank: Banka, jejíž podmínky pro bonusovou sazbu jsou kontrolovány
        :param deposit: Částka vkladu uživatele
        :param transactions: Počet transakcí uživatele
        :param investment: Výše měsíčního investování uživatele
        :return: True, pokud jsou splněny podmínky pro bonusovou sazbu, jinak False
        """
    terms = bank["bonus_terms"]

    # Check fo minimum card transactions
    if "card_transactions" in terms and transactions < terms["card_transactions"]:
        return False

    # Check for minimum deposit
    if "min_deposit" in terms and deposit < terms["min_deposit"]:
        return False

    # Check for maximum deposit
    if "max_deposit" in terms and deposit > terms["max_deposit"]:
        return False

    # Check for monthly investments
    if "investment_commitment_monthly" in terms and investment < terms["investment_commitment_monthly"]:
        return False

    return True
