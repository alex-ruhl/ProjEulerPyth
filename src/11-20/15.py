# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20×20 grid?

from math import factorial


def latticepaths(n):
    n = 2*n
    k = n/2

    return factorial(n)/(factorial(k)*factorial(n-k))


print(latticepaths(20))
