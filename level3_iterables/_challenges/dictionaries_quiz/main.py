import random

capitalsQuestions = {
    1:  {"question": "Spain", "type": "cityAns", "answer": "MADRID", "points": 1},
    2:  {"question": "Rome", "type": "countryAns", "answer": "ITALY", "points": 1},
    3:  {"question": "England", "type": "cityAns", "answer": "LONDON", "points": 1},
    4:  {"question": "Ottawa", "type": "countryAns", "answer": "CANADA", "points": 2},
    5:  {"question": "France", "type": "cityAns", "answer": "PARIS", "points": 1},
    6:  {"question": "Athens", "type": "countryAns","answer": "GREECE", "points": 1},
    7:  {"question": "India", "type": "cityAns", "answer": "NEW DELHI", "points": 1},
    8:  {"question": "Tokyo", "type": "countryAns","answer": "JAPAN", "points": 1},
    9:  {"question": "Ireland", "type": "cityAns", "answer": "DUBLIN", "points": 2},
    10: {"question": "Mexico City", "type": "countryAns", "answer": "MEXICO", "points": 0.5}
}



def game():

    gameQuestions = {} #initialise game questions
    for n in range(1, 6):
        gameQuestions[n] = capitalsQuestions[random.randint(1,10)]

    totalPoints = 0 #initialise points

    for QNumber, QDetails in gameQuestions.items(): #iterates through gameQuestions
        if QDetails["type"] == "cityAns":
            if QNumber == 1:
                response = input(f"Q{QNumber}: What is the capital of {QDetails["question"]}? ({QDetails["points"]} point(s))(enter here): ")
            else:
                response = input(f"Q{QNumber}: What is the capital of {QDetails["question"]}? ({QDetails["points"]} point(s)): ")
        elif QDetails["type"] == "countryAns":
            if QNumber == 1:
                response = input(f"Q{QNumber}: {QDetails["question"]} is the capital of what country? ({QDetails["points"]} point(s))(enter here): ")
            else:
                response = input(f"Q{QNumber}: {QDetails["question"]} is the capital of what country? ({QDetails["points"]} point(s)): ")
        
        if response.upper() == QDetails["answer"]:
            totalPoints+= QDetails["points"]
            print(f"Correct answer! You got {QDetails["points"]} point(s)!")
            print()
        else:
            print("Incorrect answer. Better luck next time.")
            print()
    
    print(f"In total, you got {totalPoints} points!")




print("Welcome to the capital city quiz!")
print("\n\
In this quiz you will be quizzed on a random select of countries and their capitals. You will be scored depending on\n\
how hard the questions were and how well you did. The number of points you score for getting a question right is variable\n\
depending on how hard the question is and will show on the question.\
\n")

game()