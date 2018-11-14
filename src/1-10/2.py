countN = 4000000
table = []
table.append(0)
table.append(1)

def dynamicFibo(n, table = []):
    while len(table) < n+1: table.append(0)
    #base case
    if n <= 1:
        return n
    #recursive case
    else:
        if table[n-1] == 0:
            table[n-1] = dynamicFibo(n-1)

        if table[n-2] == 0:
            table[n-2] = dynamicFibo(n-2)

        table[n] = table[n-2] + table[n-2]

    return table[n]


dynamicFibo(countN, table)


for i in range(0, len(table)):
    print(table[i])