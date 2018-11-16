import math

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def max_p_factor(n):

    m_p_factor = -1

    while n % 2 == 0:
        m_p_factor = 2
        n /= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            m_p_factor = i
            n /= i

    if n > 2:
        m_p_factor = n

    return int(m_p_factor)


n = 600851475143
print(max_p_factor(n))
