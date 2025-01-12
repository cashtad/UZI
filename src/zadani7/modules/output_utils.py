def print_dividing_line():
    print("\n\n---------------------------------")

def print_result(bank, explanation):
    if bank is None:
        print(f"\n\nNeexistují žádné banky, které by vyhovovaly vašim podmínkám")
        return
    print(f"\n\nVybraná banka: {bank['name']}.\n{explanation}")