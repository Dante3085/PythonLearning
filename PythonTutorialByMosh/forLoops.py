
for char in "Python":
    print(char)

for item in ["Peter", "Siglinde", "Moritz"]:
    print(item)

numbers = [5, 123, 3, 5]
for number in numbers:
    print(number)

# range(10) produces list [0, 1, ..., 9]
for number in range(10):
    print(number)

for number in range(10, 20):
    print(number)

for number in range(0, 10, 2):
    print(number)

prices = [10, 20, 30]
sum_total = 0
for price in prices:
    sum_total += price
print(f"Sum_total of prices: {sum_total}")