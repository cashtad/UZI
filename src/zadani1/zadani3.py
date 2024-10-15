greetings = {"Hi": "Hello", "Ahoj": "Zdravim", "Привет": "Здравствуй", "Cio": "Cio", "Ni hao": "Ni hao! Ni hao ma?"}

greeting = input()
if greeting in greetings.keys():
    print(greetings.get(greeting))
else:
    print("I don't understand you")
