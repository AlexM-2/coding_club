import random

#gets the words from the words file
original_words = []
with open("level4/_challenges/unscramble_word/original_words.txt") as words_file:
    original_words = words_file.readlines()

def scramble(word: str):
    scrambled_word = None

    while True:
        char_list = list(word) #convert the original word to a list to be shuffled
        random.shuffle(char_list) #shuffle the list version of the original word

        scrambled_word = "".join(char_list) #convert the list back into a string

        #checks if the scrambled word is the same as the original word or if the length of the word is 1 letter
        if not scrambled_word == word or len(char_list) == 1: 
            break #exit the loop; if it doesn't pass the if statement, the while loop will continue again

    return scrambled_word

print("This is an unscramble the word game!")


def main():

    print()

    #find a random word in the word list and remove the whitespace
    chosen_word = random.choice(original_words).rstrip()

    scrambled_word = scramble(chosen_word) #scramble the chosen word

    print(f"The scrambled word: {scrambled_word}")

    response = input(f"Enter your guess (enter q to give up, x to exit): ")
    if response.lower() == "q":
        print(f"The word was {chosen_word}")
    elif response.lower() == "x":
        raise SystemExit
    elif response.lower() == chosen_word.lower():
        print("Correct answer!")
    else:
        print("Incorrect answer. The word was " + chosen_word)

while True:
    main()