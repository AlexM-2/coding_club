import random
import time

choices = ["Heads", "Tails"]

while True:
    coin = random.choice(choices)

    while True:
        coinGuess = input("Do you think the coin will land on heads or tails? (h/t): ").capitalize()

        if (coinGuess == "H" or coinGuess == "Heads") or (coinGuess == "T" or coinGuess == "Tails"):
            print()
            print("Rolling the coin...")
            time.sleep(random.random())
            time.sleep(random.random())
            print("...")
            time.sleep(random.random())
            time.sleep(random.random())

            print(f"It's {coin}!")
            
            if coinGuess == "H":
                coinGuess = "Heads"
            elif coinGuess == "T":
                coinGuess = "Tails"
            
            if coinGuess == coin:
                print("You guessed right!")
            else:
                print("Better luck next time.")
            
            playAgain = input("Would you like to play again? (y/n): ").capitalize()
            if playAgain == "Y" or playAgain == "Yes":
                print()
                break
            else:
                print()
                print("="*100)
                print()
                exit()
        else:
            print("Invalid answer. Try again.")