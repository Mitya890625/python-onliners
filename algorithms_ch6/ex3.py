## The Data
n = 5
## The One-Liner
factorial = lambda n: n * factorial(n-1) if n > 1 else 1
## The Result
print(factorial(n))



def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(10))
