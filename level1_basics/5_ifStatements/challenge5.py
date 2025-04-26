number = 0

guess_number = float(input("Guess my number: "))

if guess_number == number:
    print("You guessed it!")
elif guess_number > number:
    print("Your guess is too high!")
elif guess_number < number:
    print("Your guess is too low!")
else:
    print("ERROR")