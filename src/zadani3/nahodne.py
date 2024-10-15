import random

number = random.randint(0,100)
print(f"Nahodnim cislem je: {number}")
if number <= 50:
    print("Male cislo")
else:
    print("Velke cislo")