number = input("Enter your number:")

try:
    number = int(number)
    if number.is_integer() == 0:
        print("Please enter an integer")
        exit()
    if number < 0:
        print("Please enter a positive number")
        exit()
except ValueError:
    print("Please enter a positive integer")
    exit()
factorial = 1
for i in range(1, number + 1):
    factorial *= i
else:
    print(factorial)