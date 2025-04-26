import random

highScore = 0
score = 0

capitals = [ #creates a list of all the countries and capitals the progr
    ("China", "Beijing"),
    ("England", "London"),
    ("France", "Paris"),
    ("Greece", "Athens"),
    ("India", "New Delhi"),
    ("Italy", "Rome"),
    ("Mexico", "Mexico City"),
    ("Portugal", "Lisbon"),
    ("Russia", "Moscow"),
    ("Scotland", "Edinburgh"),
    ("Spain", "Madrid"),
    ("United States", "Washington DC"),
    ("Wales", "Cardiff"),
    ("Poland", "Warsaw"),
    ("Norway", "Oslo"),
    ("New Zealand", "Wellington"),
    ("Netherlands", "Amsterdam"),
    ("Kenya", "Nairobi"),
    ("Japan", "Tokyo"),
    ("Ireland", "Dublin")
]

playing = True

print("This is a quiz on capital cities.")
print("You must have perfect spelling in your answers.")

while playing == True:
    results = []
    score = 0
    question = 0

    random.shuffle(capitals)
    capitalsCopy = capitals

    game_capitals = []
    num = 0
    for capital in capitals:
        if num == 5:
            continue
        question_details = capitalsCopy.pop(num)
        game_capitals.append(question_details)

        num+= 1
    
    print()
    print("Here are the questions:")
    print()

    for country, capital in game_capitals:
        question+= 1
        if random.randint(0, 1) == 0:
            print(f"Q{question}: What is the capital city of {country}?")
            answer = input("\tA: ")

            if answer == capital:
                score+= 1
            results.append((country, capital, answer, question, True))
            print((country, capital, answer, question, True))
        else:
            print(f"Q{question}: Which country is {capital} the capital city of?")
            answer = input("\tA: ")

            if answer == country:
                score+= 1
            results.append((country, capital, answer, question, False))
            print((country, capital, answer, question, False))
    print()
    print("Here are your results:")
    print()
    question = 0
    for country, capital in game_capitals:
        question+=1
        if results[question-1][4] == True:
            if results[question-1][2].lower() == capital.lower():
                print(f"Q{question}: What is the capital city of {country}?")
                print(f"\tYour answer: {results[question-1][2]} - Correct!")
            else:
                print(f"Q{question}: What is the capital city of {country}?")
                print(f"\tYour answer: {results[question-1][2]} - Incorrect. Correct answer: {capital}")
        else:
            if results[question-1][2].lower() == country.lower():
                print(f"Q{question}: Which country is {capital} capital city of?")
                print(f"\tYour answer: {results[question-1][2]} - Correct!")
            else:
                print(f"Q{question}: Which country is {capital} capital city of?")
                print(f"\tYour answer: {results[question-1][2]} - Incorrect. Correct answer: {capital}")
    print(f"Score: {score}/5")
    if score > highScore:
        highScore = score
    print(f"Highscore: {highScore}")
    print()
    playAgain = input("Would you like to play again? (y/n): ").lower()
    if playAgain == "y" or playAgain == "yes":
        playing = True
    else:
        playing = False