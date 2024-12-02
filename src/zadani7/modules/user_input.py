def get_user_input():
    deposit = float(input("Введите сумму депозита (CZK): "))
    transactions = int(input("Введите количество транзакций по карте в месяц: "))
    investment = float(input("Готовы ли вы инвестировать ежемесячно? Если да, укажите сумму (CZK), иначе 0: "))
    return deposit, transactions, investment