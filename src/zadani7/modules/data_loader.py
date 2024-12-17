import json


# Modul: data_loader.py
# Úloha: Znalostní systém pro výběr nejlepší banky pro spořicí účet
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 01.12.2024

# Tento modul se používá pro načítání dat o bankách z externího souboru ve formátu JSON.


def load_bank_data(filepath):
    """
        Funkce načítá data o bankách ze souboru ve formátu JSON.
        :param filepath: Cesta k souboru s daty o bankách
        :return: Seznam bank načtený ze souboru
        """
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)
