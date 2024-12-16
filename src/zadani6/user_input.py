from output import vypis_informace_o_bytu, vypis_informace_o_mistnosti, vypis_informace_o_oknech, \
    vypis_informace_o_vsech_mistnostech


def zpracuj_prikaz(prikaz, byt):
    """
    Zpracuje uživatelský příkaz.
    """
    if prikaz == "/info":
        vypis_informace_o_bytu(byt)
    elif prikaz == "/rooms":
        vypis_informace_o_vsech_mistnostech(byt)
    elif prikaz.startswith("/room"):
        try:
            _, nazev = prikaz.split(maxsplit=1)
            vypis_informace_o_mistnosti(byt, nazev)
        except ValueError:
            print("Neplatný příkaz.")
    elif prikaz == "/windows":
        vypis_informace_o_oknech(byt)

    else:
        print("Neplatný příkaz.")
