
help_string = '''start - to start the car
stop - to stop the car
quit - to exit'''

user_input = ""

while True:
    user_input = input(">").upper()

    if user_input == "HELP":
        print(help_string)
    elif user_input == "START":
        car_started = True
        print("Car started...Ready to go!")
    elif user_input == "STOP":
        car_started = False
        print("Car stopped.")
    elif user_input == "QUIT":
        break
    else:
        print("I don't understand that...")