# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


def genprimes(limit):   # derived from
                        # Code by David Eppstein, UC Irvine, 28 Feb 2002
    d = {}              # http://code.activestate.com/recipes/117119/
    q = 2               # sieve of Erastosthenes

    while q <= limit:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1


def sumprimes(limit):
    p = genprimes(limit)
    prms = [i for i in p]
    sum = 0

    for i in range(0, len(prms)):
        sum += prms[i]

    return sum


n = 2000000
print(sumprimes(n))
