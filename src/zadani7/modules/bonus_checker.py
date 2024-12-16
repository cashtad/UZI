def check_bonus_conditions(bank, deposit, transactions, investment):
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
