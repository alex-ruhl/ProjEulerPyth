sumMultiples = 0

for x in range(1, 1000):
    if x % 3 == 0:
        sumMultiples += x
    elif x % 5 == 0:
        sumMultiples += x

print(sumMultiples)