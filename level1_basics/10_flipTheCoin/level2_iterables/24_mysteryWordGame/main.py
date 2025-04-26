import random
import time

wordList = [
    "incomprehensibilities", 
    "honorificabilitudinitatibus", 
    "interdisciplinary", 
    "inconsequential", 
    "floccinaucinihilipilification", 
    "antidisestablishmentarianism", 
    "pneumonoultramicroscopicsilicovolcanoconiosis",
    "supercalifragilisticexpialidocious"
    ]

print("This is a mystery word length game. You need to guess the length of the computer-generated word. You have 3 attempts. \nYou will get told after each attempt whether your guess is longer or shorter than the correct length.")

attempts = 0

while True:
    if attempts >= 3:
        print()
        print("You have run out of attempts")
        print(f"The correct word was '{correct_word}' with {correct_length} letters.")
        print()
        playAgain = input("Would you like to play again? (y/n): ").lower()
        if playAgain == "y":
            attempts = 0
        elif playAgain != "y":
            print()
            print("="*100)
            print()
            exit()            

    correct_word = random.choice(wordList)
    correct_length = len(list(correct_word))

    while attempts < 3:

        attempts+= 1

        print()
        guess_length = int(input("Guess the length of my word: "))
        if guess_length == correct_length:
            attempts = 0
            print()
            print("Congratulations, you are correct.")
            print(f"The word was '{correct_word}' with {correct_length} letters.")
            print()

            time.sleep(1)

            playAgain = (input("Would you like to play again? (y/n): ")).lower()
            if playAgain == "y":
                attempts = 0
                break
            else:
                print()
                print("="*100)
                print()
                exit()

        elif guess_length > correct_length:
            print("Too long")
        elif guess_length < correct_length:
            print("Too short")
        else:
            print("ERROR")
            exit()