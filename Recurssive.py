# n = 0
# f = 1
# for i in range(1,n+1):
#     f = f * i
# print(f)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = 6
print(f"Factorial of {n}: {factorial(n)}")

def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)

n = 5
print(f"Sum Of {n}: {find_sum(5)}")


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

n = 6
print(f"Fibonacci of {n}: {fib(n)}")