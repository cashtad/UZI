import json
from data import Byt, Mistnost, Okno, Dvere

def nacti_data(soubor):
    """
    Načte data z textového souboru ve formátu JSON a vytvoří instance příslušných tříd.
    """
    with open(soubor, "r", encoding="utf-8") as f:
        data = json.load(f)

    byt = Byt(
        adresa=data["adresa"],
        plocha_celkova=data["plocha_celkova"],
        mistnosti=[]
    )

    for mistnost_data in data["mistnosti"]:
        mistnost = Mistnost(
            nazev=mistnost_data["nazev"],
            plocha=mistnost_data["plocha"],
            nabytek=mistnost_data["nabytek"],
            okna=[
                Okno(okno["nazev"], okno["strana"], okno["vyska"], okno["sirka"])
                for okno in mistnost_data.get("okna", [])
            ],
            dvere=[
                Dvere(
                    dvere["nazev"], dvere["vyska"], dvere["sirka"], dvere["z_mistnosti"], dvere["do_mistnosti"]
                )
                for dvere in mistnost_data.get("dvere", [])
            ]
        )
        byt.mistnosti.append(mistnost)

    return byt