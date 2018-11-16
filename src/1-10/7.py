def nthprime(n):
    firstprime = 2
    return firstprime + (n * 2) - 1


print(nthprime(10001))