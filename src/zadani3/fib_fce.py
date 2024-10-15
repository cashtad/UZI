

def fibonacci(n):
    if n <= 1:
        return n
    cislo = fibonacci(n - 1) + fibonacci(n - 2)
    a.append(cislo)
    return cislo

a = []