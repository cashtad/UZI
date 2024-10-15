count = 0
i = 1
while count < 20:
    number = i * 5
    i = i + 1
    if number % 3 == 0:
        continue
    else:
        print(number)
        count = count + 1
