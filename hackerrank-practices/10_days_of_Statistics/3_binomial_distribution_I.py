def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)


def combination(n, x):
    return factorial(n) / (factorial(x) * factorial(n - x))


def binomial(x, n, p):
    return combination(n, x) * p ** x * (1 - p) ** (n - x)


l, r = list(map(float, input().split(" ")))
odds = l / r
print(round(sum([binomial(i, 6, odds / (1 + odds)) for i in range(3, 7)]), 3))
