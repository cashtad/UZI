# Autor: Leonid Malakhov
# Dne: 17.10.2024
# ZADANI 3
# Program dostane na vstupu pozdravy a odpoví na ně pozdravem v českém jazyce.

def respond_to_greeting():
    responses = {
        "Ahoj": "Ahoj! Jak se máš?",
        "Dobrý den": "Dobrý den! Jak vám mohu pomoci?",
        "Čau": "Čau! Co je nového?",
        "Nazdar": "Nazdar! Jak to jde?",
        "Zdravím": "Zdravím vás! Jak se dnes máte?"
    }

    # Standardní odpověď, pokud není pozdrav rozpoznán
    default_response = "Promiňte, nerozumím vašemu pozdravu. Můžete to prosím zopakovat?"

    # Nacitani pozdravu od uzivatele
    greeting = input("Zadejte svůj pozdrav: ")

    if greeting == '`':
        exit(0)

    # Vrácení odpovědi na základě pozdravu
    print(responses.get(greeting, default_response))


print("Autor: LEONID MALAKHOV. \nTento program na uvítání vhodně reaguje. Podporované pozdravy: \n"
      "Ahoj, Dobrý den, Čau, Nazdar, Zdravím")
print("Pro ukončení programu napište '`'.")

# Запуск функции
while True:
    respond_to_greeting()
