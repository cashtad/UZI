def check_bonus_conditions(bank, deposit, transactions, investment):
    terms = bank["bonus_terms"]

    # Проверка минимального количества транзакций
    if "card_transactions" in terms and transactions < terms["card_transactions"]:
        return False

    # Проверка минимальной суммы депозита
    if "min_deposit" in terms and deposit < terms["min_deposit"]:
        return False

    # Проверка максимальной суммы депозита
    if "max_deposit" in terms and deposit > terms["max_deposit"]:
        return False

    # Проверка обязательного ежемесячного инвестирования
    if "investment_commitment_monthly" in terms and investment < terms["investment_commitment_monthly"]:
        return False

    return True
