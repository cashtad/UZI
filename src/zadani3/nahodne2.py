import random

number = random.randint(0, 500)
print(f"Nahodnim cislem je: {number}")
if number <= 150:
    print("Male cislo")
elif number <= 350:
    print("Průměrné číslo")
else:
    print("Velké číslo")
