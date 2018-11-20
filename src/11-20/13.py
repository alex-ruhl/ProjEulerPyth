# Work out the first ten digits of the sum of
# the following one-hundred 50-digit numbers.


def largesum(digits, numbers):
    sum = 0
    for n in numbers:
        sum += int(n)
    res = str(sum)
    return int(res[:-(len(res) - digits)])


numbers = []
file = open("13.txt", "r")
for line in file:
    numbers.append(line[:-1])
file.close()

print(largesum(10, numbers))
