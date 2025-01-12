# Modul: bank_filter.py
# Úloha: Znalostní systém pro výběr nejlepší banky pro spořicí účet
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 01.12.2024
# Tento modul obsahuje funkce pro filtrování bank podle základních podmínek vkladu a geografické dostupnosti poboček.
# Funkce umožňují vybrat banky, které splňují podmínky minimálního a maximálního vkladu a mají pobočky v požadovaných městech.

def filter_banks_by_basic_conditions(banks, deposit):
    """
        Funkce filtruje banky na základě minimálního a maximálního vkladu.
        :param banks: Seznam bank s jejich podmínkami
        :param deposit: Zadaný vklad uživatele
        :return: Seznam bank, které splňují podmínky vkladu
        """
    return [bank for bank in banks if deposit >= bank["min_deposit"] and
            (bank["max_deposit"] is None or deposit <= bank["max_deposit"])]


def filter_banks_by_city(banks, city_info):
    """
        Funkce filtruje banky na základě poboček v uživatelem zadaných městech.
        :param banks: Seznam bank s informacemi o pobočkách
        :param city_info: Seznam měst, ve kterých má uživatel zájem o pobočku
        :return: Seznam bank, které mají pobočky v požadovaných městech
        """
    if city_info is None:
        return banks

    city, nearest_large_city = city_info  # Extracting city and nearest large city
    filtered_banks = []

    for bank in banks:
        branch_cities = bank["branches"].keys()

        # Check if the bank has branches in the required cities
        if city in branch_cities or nearest_large_city in branch_cities:
            filtered_banks.append(bank)

    return filtered_banks


def filter_banks(banks, deposit, city_info):
    """
       Funkce kombinuje základní a geografické filtrování pro získání vhodných bank.
       :param banks: Seznam bank s podmínkami
       :param deposit: Zadaný vklad uživatele
       :param city_info: Seznam měst, ve kterých má uživatel zájem o pobočku
       :return: Seznam bank, které splňují všechny podmínky
       """
    filtered_banks = filter_banks_by_basic_conditions(banks, deposit)
    if city_info is not None:
        filtered_banks = filter_banks_by_city(filtered_banks, city_info)
    return filtered_banks
