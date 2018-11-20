# Work out the first ten digits of the sum of
# the following one-hundred 50-digit numbers.

numbers = []
file = open("13.txt", "r")
for line in file:
    numbers.append(line[:-1])
file.close()

print(numbers)
