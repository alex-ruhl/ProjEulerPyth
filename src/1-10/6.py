import math


def sumsquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += int(math.pow(i, 2))
    return sum


def squaresum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return int(math.pow(sum, 2))


count = 100
temp = sumsquares(count)
temp1 = squaresum(count)
print(temp1 - temp)