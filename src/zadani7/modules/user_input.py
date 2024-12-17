# Modul: user_input.py
# Úloha: Znalostní systém pro výběr nejlepší banky pro spořicí účet
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 01.12.2024

# Tento modul se stará o komunikaci s uživatelem a získání vstupních údajů pro rozhodování.


def get_user_input():
    """
        Funkce získává vstupní údaje od uživatele pro výběr nejlepší banky.
        :return: Částka vkladu, počet transakcí, měsíční investice a informace o městě pro pobočku
        """
    deposit = 0
    while True:
        try:
            deposit = float(input("Zadejte částku vkladu (CZK): "))
            break
        except ValueError:
            print("Nesprávný vstup. Zadejte číslo!")
    transactions = 0
    while True:
        try:
            transactions = int(input("Zadejte počet transakcí kartou za měsíc: "))
            break
        except ValueError:
            print("Nesprávný vstup. Zadejte číslo!")

    investment = 0
    while True:
        try:
            investment = float(input("Jste ochotni měsíčně investovat? Pokud ano, zadejte částku (CZK), jinak 0: "))
            break
        except ValueError:
            print("Nesprávný vstup. Zadejte číslo!")

    city_info = None
    has_branch = input(
        "Je pro vás důležité mít pobočku banky ve vašem nebo nejbližším k vám městě? (ano/ne): ").strip().lower()
    if has_branch == "ano":
        city = input("Zadejte název vašeho města: ")
        nearest_large_city = input("Jaké je nejbližší velké město? ")
        city_info = [city, nearest_large_city]

    return deposit, transactions, investment, city_info
