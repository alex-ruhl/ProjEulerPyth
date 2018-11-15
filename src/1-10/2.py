countN = 4000000

# goes through every fib number => slow
# solution: skip primes
# def sumevenfibonacci(n):
#     a = 0
#     b = 1
#     c = 0
#     sumeven = 0
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 0
#     else:
#         while c < n:
#             c = a + b
#             if c % 2 == 0:
#                 sumeven += c
#             a = b
#             b = c
#         return sumeven

def sumevenfibonacci(n):
    a = 1
    b = 1
    c = a + b
    sumeven = 0
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 0
    else:
        while c < n:
            sumeven += c
            a = b + c
            b = c + a
            c = a + b
        return sumeven


print(sumevenfibonacci(countN))
