# Modul: user_input.py
# Úloha: Znalostní systém pro výběr nejlepší banky pro spořicí účet
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 01.12.2024
import re


# Tento modul se stará o komunikaci s uživatelem a získání vstupních údajů pro rozhodování.


def get_complete_user_input():
    """
        Funkce získává vstupní údaje od uživatele pro výběr nejlepší banky.
        :return: Částka vkladu, počet transakcí, měsíční investice a informace o městě pro pobočku
        """
    while True:
        try:
            deposit = float(input("Zadejte částku vkladu (CZK): "))
            if deposit > 0:
                break
            else:
                print("Nesprávný vstup. Zadejte číslo > 0!")

        except ValueError:
            print("Nesprávný vstup. Zadejte číslo!")
    while True:
        try:
            transactions = int(input("Zadejte počet transakcí kartou za měsíc: "))
            if transactions >= 0:
                break
            else:
                print("Nesprávný vstup. Zadejte číslo >= 0!")

        except ValueError:
            print("Nesprávný vstup. Zadejte číslo!")

    while True:
        try:
            investment = float(input("Jste ochotni měsíčně investovat? Pokud ano, zadejte částku (CZK), jinak 0: "))
            break
        except ValueError:
            print("Nesprávný vstup. Zadejte číslo!")

    city_info = None
    while True:
        has_branch = input(
            "Je pro vás důležité mít pobočku banky ve vašem nebo nejbližším k vám městě? (ano/ne): ").strip().lower()
        if has_branch == "ano":
            while True:
                city = input("Zadejte název vašeho města: ").strip()
                if not validate_city_name(city):
                    print("Zadaný název města je neplatný.")
                else:
                    break
            while True:
                nearest_large_city = input("Zadejte název vašeho nejbližšího velkého města: ").strip()
                if not validate_city_name(nearest_large_city):
                    print("Zadaný název města je neplatný.")
                else:
                    break
            city_info = [city, nearest_large_city]
            break
        elif has_branch == "ne":
            break
        else:
            print("Nesprávný vstup. Zadejte 'ano' nebo 'ne'.")

    return deposit, transactions, investment, city_info

def validate_city_name(city_name):
    """
    Проверяет, является ли введённое название города корректным.

    Условия:
    1. Название должно содержать только буквы чешского алфавита, пробелы и дефисы.
    2. Длина названия должна быть от 2 до 100 символов.
    3. Название должно начинаться с буквы.

    :param city_name: str - название города
    :return: bool - True, если название корректное, иначе False
    """
    # Чешский алфавит с учётом диакритических знаков
    pattern = r"^[A-Za-zÁáČčĎďÉéĚěÍíŇňÓóŘřŠšŤťÚúŮůÝýŽž][A-Za-zÁáČčĎďÉéĚěÍíŇňÓóŘřŠšŤťÚúŮůÝýŽž\s\-]{1,99}$"
    return bool(re.match(pattern, city_name.strip()))

def get_start_again_input():
    return input("\nStisknutím klávesy ENTER začněte znovu nebo zadejte 'EXIT' pro ukončení: ")

