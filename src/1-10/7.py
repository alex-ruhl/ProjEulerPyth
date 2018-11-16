import math


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


def nthprime(n):
    p = genprimes(n * int(math.sqrt(n)))
    prms = [i for i in p]

    return prms[n-1]


nth = 10001
print(nthprime(nth))
