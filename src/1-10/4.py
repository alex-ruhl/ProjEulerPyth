def largest_palindrome(n):
    l_pal = 0
    factor_max = 9
    factor_floor = 1

    for i in range(1, n):
        factor_floor *= 10
        factor_max = factor_max * 10 + 9

    factor_one = factor_max

    while factor_one > factor_floor:
        factor_two = factor_max
        while factor_two >= factor_one:
            if factor_one * factor_two <= l_pal:
                break

            temp = factor_one * factor_two
            if is_palindrome(str(temp)):
                l_pal = temp

            factor_two -= 1
        factor_one -= 1

    return l_pal


def is_palindrome(n):
    """
    :type n: String
    """
    return n == n[::-1]


digits = 3
print(largest_palindrome(digits))
