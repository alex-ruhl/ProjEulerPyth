import math
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pythagoreantriplet(target):

    for a in range(1, target):
        for b in range(a, target):
            for c in range(b, target):
                if a*a + b*b == c*c:
                    if a + b + c == target:
                        return a * b * c


print(pythagoreantriplet(1000))
