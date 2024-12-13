def vypis_informace_o_bytu(byt):
    """
    Vypíše informace o bytě.
    """
    print(f"Adresa: {byt.adresa}")
    print(f"Celková plocha: {byt.plocha_celkova} m²")
    print(f"Počet místností: {len(byt.mistnosti)}")

def vypis_informace_o_mistnosti(byt, nazev):
    """
    Vypíše informace o místnosti dle jejího názvu.
    """
    for mistnost in byt.mistnosti:
        if mistnost.nazev == nazev:
            print(f"Místnost: {mistnost.nazev}")
            print(f"Plocha: {mistnost.plocha} m²")
            print(f"Nábytek: {mistnost.nabytek}")
            for okno in mistnost.okna:
                print(f"Okno: {okno.nazev}, Strana: {okno.strana}, Rozměry: {okno.vyska}x{okno.sirka} m")
            for dvere in mistnost.dvere:
                print(f"Dveře: {dvere.nazev}, Rozměry: {dvere.vyska}x{dvere.sirka} m, Z: {dvere.z_mistnosti}, Do: {dvere.do_mistnosti}")
            return
    print("Místnost nenalezena.")

def vypis_informace_o_oknech(byt):
    """
    Vypíše informace o všech oknech v bytě.
    """
    for mistnost in byt.mistnosti:
        for okno in mistnost.okna:
            print(f"Okno: {okno.nazev}, Místnost: {mistnost.nazev}, Strana: {okno.strana}")

def vypis_informace_o_vsech_mistnostech(byt):
    """
    Vypíše názvy všech místností v bytě.
    """
    print("Místnosti v bytě:")
    for mistnost in byt.mistnosti:
        print(f"- {mistnost.nazev}")