def dig_sum(n):
    summ = 0
    n = pow(2, n)
    while n > 0:
        summ += n % 10
        n //= 10
    return summ


print(dig_sum(1000))
