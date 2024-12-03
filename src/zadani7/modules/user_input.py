def get_user_input():
    deposit = float(input("Zadejte částku vkladu (CZK): "))
    transactions = int(input("Zadejte počet transakcí kartou za měsíc: "))
    investment = float(input("Jste ochotni měsíčně investovat? Pokud ano, zadejte částku (CZK), jinak 0: "))

    city_info = None
    has_branch = input("Je pro vás důležité mít pobočku banky ve vašem městě? (ano/ne): ").strip().lower()
    if has_branch == "ano":
        city = input("Zadejte název vašeho města: ")
        nearest_large_city = input("Jaké je nejbližší velké město? ")
        city_info = (city, nearest_large_city)

    return deposit, transactions, investment, city_info
