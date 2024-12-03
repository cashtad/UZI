def filter_banks_by_basic_conditions(banks, deposit):
    return [bank for bank in banks if deposit >= bank["min_deposit"] and
            (bank["max_deposit"] is None or deposit <= bank["max_deposit"])]


def filter_banks_by_city(banks, city_info):
    if city_info is None:
        # Если city_info равно None, вернуть все банки
        return banks

    city, nearest_large_city = city_info  # Извлекаем город и ближайший крупный город
    filtered_banks = []

    for bank in banks:
        # Получаем все города, где есть отделения данного банка
        branch_cities = bank["branches"].keys()

        # Проверяем, есть ли хотя бы одно отделение в нужных городах
        if city in branch_cities or nearest_large_city in branch_cities:
            filtered_banks.append(bank)

    return filtered_banks