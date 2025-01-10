import math

# Author: Leonid Malakhov
# Program will find all prime numbers that are smaller than entered numbers using Sieve of Eratosthenes


# Input
print("This algorithm will find all prime numbers that are smaller than entered number\n\n")
while True:
    number = input("Enter the number to find all prime numbers that are smaller: ")
    try:
        number = int(number)
        if number.is_integer() == 0:
            print("Please enter an integer")
            continue
        if number < 0:
            print("Please enter a positive number")
            continue
        if number < 3:
            print("There is no prime number smaller")
            continue
        break
    except ValueError:
        print("Please enter a positive integer")
        continue


# At the beginning it will initialize array with only one prime number - 2
arr = [2]

# Then it will add all numbers that cannot be devided by 2 until inputted number
for i in range(3, int(number)):
    if i % 2 == 1:
        arr.append(i)

# Then it will go through the array and remove all numbers that are not real
for i in arr:

    # If number is bigger than square of inputted number the cyckle will stop
    if i > math.sqrt(number):
        break
    for j in arr:
        if j % i == 0 and i != j:
            arr.remove(j)

print("\nPrime numbers that are smaller than entered number", arr)

input("\n\nPress ENTER to exit")