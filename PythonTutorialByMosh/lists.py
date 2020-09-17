
names = ["John", "Bob", "Moritz", "Peter", "Sarah"]

'''
list[lower_index:upper_index]
- Returns all elements in the range specified by lower and upper_index.
- lower_index is inclusive. upper_index is exclusive(it's element will not be returned).
- lower_index and upper_index can be negative numbers. -1 is the first element looking from the end of the list.
- If lower_index is left empty it is automatically set to 0.
- If upper_index is left empty it is automatically set to len(list).
'''

print(names)
print(names[2])
print(names[-2])
print(names[1:3])
print(names[1:])
print(names[1:-1])
print(names[:])

names[0] = "Derick"
print(names)

# find largest number in list
numbers = [5, 2, 3233, 3, 10, 7, 2, 999]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)