import random

# Author: Leonid Malakhov
# On startup program will ask you if you want to enter the array manually
# or let it be generated randomly with defined length (integer, entered manually)
# After entering input, program will show input array and then sorted array


print("This program will sort entered array of integers")
print("Input can be entered manually as array of integers or could be generated randomly for defined length."
      " Numbers will be in range 1,100\n")

arr = []

# Manual or random initialization of an array
while True:
    variation = input("Do you want to enter array manually or let it be generated randomly? [YES/NO]: ")

    if variation == "YES":
        while True:
            try:
                arr = input("Enter the array: ")
                arr = list(map(int, arr.split()))
                break
            except ValueError:
                print("Please enter a valid array of integers: ")
        print("Entered array: ", arr)
        break

    elif variation == "NO":
        while True:
            try:
                var = int(input("Enter the length of the array: "))
                break
            except ValueError:
                print("Please enter a valid integer")
                continue
        for i in range(var):
            value = random.randint(0, 100)
            if arr.count(value) > 0:
                continue
            else:
                arr.append(value)
        print("Generated array: ", arr)
        break

    else:
        print("Unknown input please enter either YES or NO")


# Recursive quick sort function
def quick_sort(arr):
    # Return if recursive got to the end
    if len(arr) < 2:
        return arr

    # As a pivot always will be the first element of the array
    pivot = arr[0]
    left = []
    right = []

    # Splitting the array to 2 arrays. Left one contains only small numbers (comparing to the pivot)
    # , right one - only big numbers (also by comparing it to the pivot)
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
input("\n\nPress ENTER to exit")
