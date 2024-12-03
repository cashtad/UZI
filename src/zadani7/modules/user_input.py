def get_user_input():
    deposit = float(input("Zadejte částku vkladu (CZK): "))
    transactions = int(input("Zadejte počet transakcí kartou za měsíc: "))
    investment = float(input("Jste ochotni měsíčně investovat? Pokud ano, zadejte částku (CZK), jinak 0: "))
    return deposit, transactions, investment
