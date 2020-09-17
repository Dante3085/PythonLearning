
numbers = [5, 2, 1, 7, 4]

numbers.append(13)
print(numbers)

numbers.insert(1, 20)
print(numbers)

numbers.remove(7)
print(numbers)

numbers.pop(1)
print("pop(1): " + str(numbers))

numbers.pop(-2)
print(numbers)

numbers.pop()
print(numbers)

print("numbers.index(2): " + str(numbers.index(2)))
print(2 in numbers)
print(50 in numbers)

numbers = [1, 2, 1, -10, 3, 2, 23, 44, 2]
print("numbers.count(1): " + str(numbers.count(1)))

numbers.sort()
print(numbers)

numbers2 = numbers.copy()
numbers.append(239)
print("print(numbers2): " + str(numbers2))

numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)

list_with_duplicates = [5, 3, 5, 1, 2, 48, 1, 0, 435, 3]
print("list_with_duplicates: " + str(list_with_duplicates))
uniques = []

for number in list_with_duplicates:
    if number not in list_with_duplicates:
        uniques.append(number)
print("uniques: " + str(uniques))