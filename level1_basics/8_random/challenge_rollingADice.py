import random
import time

while True:
    print("Player 1 is rolling a dice.")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    randNumber1 = random.randint(1,6)
    print(f"Player 1 rolled a {randNumber1}!")
    print()
    print("Player 2 is rolling a dice.")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    randNumber2 = random.randint(1,6)
    print(f"Player 2 rolled a {randNumber2}!")
    if randNumber1 == randNumber2:
        print()
        print("It's a tie!")
        print()
    elif randNumber1 > randNumber2:
        print()
        print("Player 1 won!")
        print()
        playAgain = input("Would you like to play again (y/n): ").capitalize()
        if playAgain == "Y":
            print()
        else:
            break
    elif randNumber2 > randNumber1:
        print()
        print("Player 2 won!")
        print()
        playAgain = input("Would you like to play again (y/n): ").capitalize()
        if playAgain == "Y":
            print()
        else:
            break