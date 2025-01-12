# Modul: main.py
# Úloha: Znalostní systém pro výběr nejlepší banky pro spořicí účet
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 01.12.2024


def get_explanation(bank, rate, reason, city_info):
    """
        Funkce generuje vysvětlení pro uživatele, proč byla vybrána konkrétní banka, a zobrazuje její podmínky.
        :param bank: Banka, která byla vybrána na základě podmínek uživatele
        :param rate: Úroková sazba, která byla pro tuto banku vybrána
        :param reason: Důvod, proč byla vybraná banka (např. dostupnost bonusové sazby)
        :param city_info: Informace o požadovaném městě pro pobočku banky
        :return: Vysvětlení, které bude zobrazeno uživateli, obsahující informace o bance, sazbě a pobočkách
        """

    if bank is None:
        explanation = "Neexistují žádné banky, které by vyhovovaly vašim podmínkám"
    else:
        explanation = (
            f"\nVybraná banka: {bank['name']}.\n"
            f"Důvod: {reason}\n"
            f"Úroková sazba: {rate}%\n"
            f"Další informace:\n"
            f"- Minimální vklad: {bank['min_deposit']} CZK\n"
            f"- Maximální vklad: {str(bank['max_deposit']) + ' CZK' if bank['max_deposit'] else 'Neomezeno'} \n"
            f"- Poplatek za vedení účtu: {bank['account_fee']} CZK/měsíc\n"
        )
        if city_info:
            try:
                explanation += f"- Nejbližší pobočka banky ve vašem městě: {bank['branches'][city_info[0]]}\n"
            except KeyError:
                explanation += f"- Nejbližší pobočka banky v nejbližším městě: {bank['branches'][city_info[1]]}\n"

    return explanation
