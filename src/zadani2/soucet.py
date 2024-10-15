r = [1,2,3,4,5]
string1 = "rada cisel je"
string2 = "jeji soucet je "
soucet = 0
for cislo in r:
    string1 += " " + str(cislo)
    soucet += cislo
string2 += str(soucet)
print(string1)
print(string2)