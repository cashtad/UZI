def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


upper = int(input("Enter an upper bound of fibonacci: "))
result = fibonacci(upper)
print(f"Result of fibonacci({upper}) = {result}")



