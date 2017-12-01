
# 피보나치 수열
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 2) +  fibonacci(n - 1)

print(fibonacci(3))

print(fibonacci(5))