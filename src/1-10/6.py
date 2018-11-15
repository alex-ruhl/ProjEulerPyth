import math


def sum(n):
    sumsquares = (2*n + 1)*(n + 1)*n // 6
    squaressum = n*(n+1) / 2
    return int(math.pow(squaressum, 2)) - sumsquares


count = 100
print(sum(count))
