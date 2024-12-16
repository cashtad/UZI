def get_explanation(bank, rate, reason, city_info):
    explanation = (
        f"Vybraná banka: {bank['name']}.\n"
        f"Důvod: {reason}\n"
        f"Úroková sazba: {rate}%\n"
        f"Další informace:\n"
        f"- Minimální vklad: {bank['min_deposit']} CZK\n"
        f"- Maximální vklad: {str(bank['max_deposit']) + ' CZK' if bank['max_deposit'] else 'Neomezeno'} \n"
        f"- Poplatek za vedení účtu: {bank['account_fee']} CZK/měsíc\n"
            )
    if city_info:
        if city_info[0]:
            explanation += f"- Nejbližší pobočka banky ve vašem městě: {bank['branches'].city_info[0]}\n"
        else:
            explanation += f"- Nejbližší pobočka banky v nejbližším městě: {city_info[1]}\n"
    return explanation
