
birth_year = input("Birth year: ")
age = 2020 - int(birth_year)
print(age)

print("type(birth_year): " + str(type(birth_year)))
print("type(age): " + str(type(age)))

# int(arg): Convert arg to integer
# float(arg)
# bool(arg)
# str()

weight_in_lbs = input("What is your weight in lb(pounds)?")
print("You weigh " + str((float(weight_in_lbs) * 0.45359237)) + "kg")