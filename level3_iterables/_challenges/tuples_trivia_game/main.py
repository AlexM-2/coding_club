import time
import random

#initialising variables
score = 0
index = 0
tuples = [
    ("Fruit", "Apple"),
    ("Car brand", "Honda"),
    ("Vegetable", "Brocoli"),
    ("Country in EU", "France"),
    ("Colour", "Orange"),
    ("Number", "6"),
    ("Letter", "F")
]
random.shuffle(tuples)

#explaining the game to the player
print("A tuple is a data structure in Python that cannot be changed. It is defined like this: (XXXXX, YYYYYY, ZZZZZZ, ...).")
time.sleep(4)
print("In this game, you are going to guess the second element of a tuple, the first element being a category of the answer.")
print("For example: ('Computer type', 'PC')")
time.sleep(4)
print()
print("You must start your answers with a capital letter if applicable and have correct spelling.")
time.sleep(1)
print()

print("Here are the questions:")
while index < len(tuples): #game loop

    #getting current tuple details
    currentTuple = tuples[index]
    currentCategory = currentTuple[0]
    correctAnswer = currentTuple[1]

    print(f"{index+1}.) Tuple: ({currentCategory}, ???)") #prints the current tuple without the answer
    print(f"\tWhat could a {currentCategory.lower()} be?") #simplifies the question by asking it without the tuple format
    
    playerAnswer = input("\tEnter answer: ")
    if correctAnswer == playerAnswer: #checks if the player got the question correct
        print("\tCorrect!")
        score+= 1
        time.sleep(2)
    else:
        print(f"\tIncorrect. Correct answer: {correctAnswer}") #displays correct answer if the player got it wrong
        time.sleep(3)
    index+= 1

print()
print(f"Here is your final score: {score}/7") #displays final score