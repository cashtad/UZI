word = input("Enter your word:")
string1 = "Slovo " + word + " se sklada z techto pismen"
count = 0
for i in word:
    count += 1
    print(str(count) + ". znak je: " + i)