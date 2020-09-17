
for x in range(4):
    for y in range(4):
        print(f"({x}, {y})")

numbers = [5, 2, 5, 2, 2]
for count in numbers:
    line = ""
    for index in range(count):
        line += "X"
    print(line)