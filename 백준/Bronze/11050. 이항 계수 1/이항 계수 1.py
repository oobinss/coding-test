n, k = map(int,input().split())

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def binomial_coefficient(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

print(binomial_coefficient(n,k))