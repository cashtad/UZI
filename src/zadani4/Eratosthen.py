from numpy import sqrt

# Author: Leonid Malakhov
# Program will find all prime numbers that are smaller than entered numbers using Sieve of Eratosthenes

print("This algorithm will find all prime numbers that are smaller than entered number")
number = int(input("Enter the number to find all prime numbers that are smaller: "))

# At the beginning it will initialize array with only one prime number - 2
arr = [2]

# Then it will add all numbers that cannot be devided by 2 until inputted number
for i in range(3, int(number)):
    if i % 2 == 1:
        arr.append(i)

# Then it will go through the array and remove all numbers that are not real
for i in arr:

    # If number is bigger than square of inputted number the cyckle will stop
    if i > sqrt(number):
        print("Prime numbers that are smaller than entered number", arr)
        exit()
    for j in arr:
        if j % i == 0 and i != j:
            arr.remove(j)
