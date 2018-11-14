countN = 4000000


def sumevenfibonacci(n):
    a = 0
    b = 1
    c = 0
    sumeven = 0
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        while c < n:
            c = a + b
            if c % 2 == 0:
                sumeven += c
            a = b
            b = c
        return sumeven


print(sumevenfibonacci(countN))
