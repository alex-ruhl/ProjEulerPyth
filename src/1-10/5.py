# divisors 9 leads to RecursionError: maximum recursion depth exceeded
# def numbers(n=1):
#     yield n
#     yield from filter(lambda x: n, numbers(n + 1))


def smallest_divisible(n):
    small_div = 0
    not_found = True
    i = 0

    while not_found:

        if small_div != 0:
            not_found = False

        for j in range(1, n+1):
            if i % j != 0:
                break
            if j == n:
                small_div = i
                break
        i += n

    return small_div


divisors = 10
for divisors in range (divisors, 20):
    print(smallest_divisible(divisors))
