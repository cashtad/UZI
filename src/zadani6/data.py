### Modul dat

class Okno:
    """
    Třída reprezentující okno.
    """
    def __init__(self, nazev, strana, vyska, sirka):
        self.nazev = nazev
        self.strana = strana
        self.vyska = vyska
        self.sirka = sirka

class Dvere:
    """
    Třída reprezentující dveře.
    """
    def __init__(self, nazev, vyska, sirka, z_mistnosti, do_mistnosti):
        self.nazev = nazev
        self.vyska = vyska
        self.sirka = sirka
        self.z_mistnosti = z_mistnosti
        self.do_mistnosti = do_mistnosti

class Mistnost:
    """
    Třída reprezentující místnost.
    """
    def __init__(self, nazev, plocha, nabytek, okna=None, dvere=None):
        self.nazev = nazev
        self.plocha = plocha
        self.nabytek = nabytek
        self.okna = okna if okna else []
        self.dvere = dvere if dvere else []

class Byt:
    """
    Třída reprezentující byt.
    """
    def __init__(self, adresa, plocha_celkova, mistnosti=None):
        self.adresa = adresa
        self.plocha_celkova = plocha_celkova
        self.mistnosti = mistnosti if mistnosti else []
