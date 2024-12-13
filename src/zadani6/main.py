from input import nacti_data
from user_input import zpracuj_prikaz

def main():
    """
    Hlavní funkce programu.
    """
    byt = nacti_data("byt.json")
    print("Vítejte v programu pro správu bytu!\n")
    print("Dostupné příkazy:")
    print("/info - Zobrazí informace o bytě")
    print("/room <název> - Zobrazí informace o konkrétní místnosti")
    print("/windows - Zobrazí informace o všech oknech")
    print("/rooms - Zobrazí názvy všech místností")
    print("/exit - Ukončí program")

    while True:
        prikaz = input("\nZadejte příkaz: ")
        if prikaz == "/exit":
            print("\nProgram ukončen.")
            break
        zpracuj_prikaz(prikaz, byt)

if __name__ == "__main__":
    main()
