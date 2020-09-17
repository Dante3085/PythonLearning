
while True:
    try:
        age = int(input("Age: "))
        income = 20000
        risk = income / age
        print(age)
    except ZeroDivisionError:
        print("Cant divide by zero")
    except ValueError:
        print("Invalid value")
