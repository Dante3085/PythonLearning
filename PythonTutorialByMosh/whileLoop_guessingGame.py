
secret_number = 9
number_of_guesses = 0
guess_limit = 3

print("Guess the number")
while number_of_guesses < guess_limit:
    if int(input()) == secret_number:
        print("You guessed right.")
        break
    number_of_guesses += 1
else: # else klausel des while statements
    print("Number of tries exceeded")