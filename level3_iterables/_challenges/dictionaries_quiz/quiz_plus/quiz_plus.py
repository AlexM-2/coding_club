import random
import os

#   BROKEN QUIZ DO NOT RUN

capitalsQuestionsTol1 = {
    "EASY": {

    },
    "MEDIUM": {
        
    },
    "HARD": {
        
    }
}
capitalsQuestionsTol2 = {
    "EASY": {

    },
    "MEDIUM": {

    },
    "HARD": {

    }
}
# cdc
# 

def initialseDict(file, tolerance):

    content = file.readlines()

    for line in content: #initialise dictionary from files
        line = line.split(",,")
        line1 = line[1].split("\t")

        line2 = line1[1].removesuffix("\n")

        finishedLine = [tuple(line1[0].split(", ")), tuple(line2.split(", "))] # [[countryName1, countryName2, countryName3], [capital(Name)1, capital(Name)2, capital(Name)3]] - there are some exceptions to binary (country and capital) eg South Africa which has 3 capital cities

        if tolerance == 1:
            if line[0] == "easy":
                capitalsQuestionsTol1["EASY"][finishedLine[0]] = finishedLine[1]
            elif line[0] == "medium":
                capitalsQuestionsTol1["MEDIUM"][finishedLine[0]] = finishedLine[1]
            elif line[0] == "hard":
                capitalsQuestionsTol1["HARD"][finishedLine[0]] = finishedLine[1]
        elif tolerance == 2:
            if line[0] == "easy":
                capitalsQuestionsTol2["EASY"][finishedLine[0]] = finishedLine[1]
            elif line[0] == "medium":
                capitalsQuestionsTol2["MEDIUM"][finishedLine[0]] = finishedLine[1]
            elif line[0] == "hard":
                capitalsQuestionsTol2["HARD"][finishedLine[0]] = finishedLine[1]


#change directory to 33_dictionariesQuiz, where the files are located
os.chdir("/Users/alexmascord/Documents/Coding/coding_club/python/33_dictionariesQuiz/")

#open file
file = open("quiz+/allCapitalsGameTol1.txt", "r")
initialseDict(file, 1)

file.close()

file = open("quiz+/allCapitalsGameTol2.txt", "r")
initialseDict(file, 2)

file.close()


#initialise game type variables
difficulty = None
tolerance = None
gameType = None
numQuestions = None
instantMarking = None

def playerFormat(list):
    num = 0
    string = ""
    for subString in list:
        num+= 1
        if num > 1:
            string = string + " and "

        string = string + str(subString).lower()

def game():
    print()

    global askDifficulty
    global askTolerance
    global askGameType
    global askNumQuestions
    global askInstantMarking

    def askDifficulty(): #DONE

        global difficulty

        if not difficulty == None:
            global difficultyNow
            difficultyNow = input(f"Would you like to keep the same difficulty of questions you had last game ({playerFormat(difficulty)}) or a different one?\nOptions: \", \", \"easy\"/\"e\", \"medium\"/\"m\", \"hard\"/\"h\", \"same\"/\"s\", \"all\"/\"a\"\nEnter here: ").upper()
        elif difficulty == None:
            difficultyNow = input("What difficulty of questions would you like your game to consist of?\nOptions: \", \" (separating multiple game modes), \"easy\"/\"e\" (eg capital of France), \"medium\"/\"m\" (eg capital of Austrailia),\n\"hard\"/\"h\" (eg capital of Azerbaijan), \"all\"/\"a\"\nEnter here: ").upper()

    def checkAskDifficulty():
        
        global difficulty
        global difficultyNow
        global list2

        list1 = difficultyNow.split(", ")
        print(f"Here be list: {list1}")
        list2 = []
        
        for subString in list1:
            if subString == "E" or subString == "EASY":
                list2.append("EASY")
            elif subString == "M" or subString == "MEDIUM":
                list2.append("MEDIUM")
            elif subString == "H" or subString == "HARD":
                list2.append("HARD")
            elif subString == "S" or subString == "SAME":
                for i in difficulty:
                    list2.append(i)
            elif subString == "A" or subString == "ALL":
                list2.append("EASY")
                list2.append("MEDIUM")
                list2.append("HARD")
            else:
                print("Invalid response. Please try again")
                print()
                askDifficulty()
                checkAskDifficulty()
        difficulty = list2

    def askTolerance(): #DONE

        global tolerance

        if not tolerance == None:
            global toleranceNow
            toleranceNow = input(f"Would you like to keep the same tolerance of answers you had last game ({playerFormat(tolerance)}) or a different one?\nOptions: \"high\"/\"h\", \"low\"/\"l\", \"same\"/\"s\"\nEnter here: ").upper()
        elif tolerance == None:
            toleranceNow = input("What tolerance (eg mexico city vs Mexico City) of answers would you like your game to consist o?\nOptions: \"high\"/\"h\"(will accept variations), \"low\"/\"l\"(will not accept variations)\nEnter here: ").upper()
        
    def checkAskTolerance():

        global tolerance
        global toleranceNow
        global list2


        list1 = toleranceNow.split(", ")
        print(f"Here be list: {list1}")
        list2 = []
        for subString in list1:
            print(subString)
            if subString == "H" or subString == "HIGH":
                list2 = "HIGH"
            elif subString == "L" or subString == "LOW":
                list2 = "LOW"
            elif subString == "S" or subString == "SAME":
                list2 = tolerance
            else:
                print()
                print("Invalid response. Please try again.")
                print(f"from checkAskTolerance: {tolerance}")
                askTolerance()
                checkAskTolerance()
        tolerance = list2
                
        
        print(f"from askTolerance: {tolerance}")
        print()

    def askGameType():

        global gameType

        if not gameType == None:
            global gameTypeNow
            gameTypeNow = input(f"Would you like to keep the same game type ({playerFormat(gameType)}) you has last game or a different one?\nOptions: \", \", \"true or false\"/\"tf\", \"multiple choice\"/\"mc\", \"written\"/\"w\", \"endless\"/\"e\", \"same\"/\"s\" \"all\"/\"a\"\nEnter here: ").upper()
        elif gameType == None:
            gameTypeNow = input("What game type would you like your game to consist of?\nOptions: \", \" (separating multiple game types), \"true or false\"/\"tf\", \"multiple choice\"/\"mc\", \"written\"/\"w\", \"endless\"/\"e\"(continue answering questions until you get one wrong), \"all\"/\"a\"\nEnter here: ").upper()


    def checkAskGameType():

        global gameTypeNow
        global gameType
        global list2


        list1 = gameTypeNow.split(", ")
        list2 = []
        for subString in list1:
            if subString == "TF" or subString == "TRUE OR FALSE":
                list2.append("TRUEFALSE")
            elif subString == "MC" or subString == "MULTIPLE CHOICE":
                list2.append("MULTIPLECHOICE")
            elif subString == "W" or subString == "WRITTEN":
                list2.append("WRITTEN")
            elif subString == "E" or subString == "ENDLESS":
                list2.append("ENDLESS")
            elif subString == "A" or subString == "ALL":
                list2.append("TRUEFALSE")
                list2.append("MULTIPLECHOICE")
                list2.append("WRITTEN")
                list2.append("ENDLESS")
            elif subString == "S" or subString == "SAME":
                for i in gameType:
                    list2.append(i)
            else:
                print()
                print("Invalid response. Please try again.")
                askGameType()
                checkAskGameType()

        gameType = list2

        print(gameType)
        print()

        # True/False DONE
        # Multiple choice
        # Written
        # Endless

    askDifficulty()
    checkAskDifficulty()

    askTolerance()
    checkAskTolerance()

    askGameType()
    checkAskGameType()

    global possibleQuestions
    global tolerance

    #initialises a set of possible countries and capital pairings
    capitalsQuestionsCopy = {}
    gameQuestions = {}
    possibleQuestions = {}
    print("Findin tolerance")
    print(f"From if statement: {tolerance}")
    if tolerance == "LOW":
        capitalsQuestionsCopy = capitalsQuestionsTol1.copy()
        for i in difficulty:
            for countries, capitals in capitalsQuestionsCopy[i].items():
                possibleQuestions[countries] = capitals
    elif tolerance == "HIGH":
        capitalsQuestionsCopy = capitalsQuestionsTol2.copy()
        for i in difficulty:
            for countries, capitals in capitalsQuestionsCopy[i].items():
                possibleQuestions[countries] = capitals
    else:
        print("ERROR")

    def askNumQuestions():

        global numQuestions
        
        if not numQuestions == None:
            global numQuestionsNow
            numQuestionsNow = input(f"Would you like to keep the same number of questions you had last game ({playerFormat(numQuestions)}) or a different one?\nOptions: \"same\"/\"s\", Any number < 0\nEnter here: ").upper()
        elif numQuestions == None:
            numQuestionsNow = input("How many questions would you like to have in your game?\nOptions: 0 < Any number < total countries and capitals\nEnter here: ").upper()

    def checkAskNumQuestions():

        global numQuestionsNow
        global numQuestions
        global list2

        list1 = numQuestionsNow.split(", ")
        list2 = []
        for subString in list1:
            if subString.isdigit():
                number = int(subString)
                if number > 0 and number < len(possibleQuestions):
                    list2 = number
                else:
                    print()
                    print("Invalid response. Please try again.")
                    askNumQuestions()
                    checkAskNumQuestions()

            else:
                print()
                print("Invalid response. Please try again.")
                askNumQuestions()
                checkAskNumQuestions()

        numQuestions = list2
        
        print()
    
    def askInstantMarking():

        global instantMarking
        
        if not instantMarking == None:
            global instantMarkingNow
            instantMarkingNow = input(f"Would you like to keep the same instant marking settings ({playerFormat(instantMarking)}) you had last game or a different one?\nOptions: \"yes\"/\"y\", \"no\"/\"n\"\nEnter here: ").upper()
        elif instantMarking == None:
            instantMarkingNow = input(f"Would you like questions to be marked instantly after answering?\nOptions: \"yes\"/\"y\", \"no\"/\"n\"\nEnter here: ").upper()

    def checkAskInstantMarking():

        global instantMarkingNow
        global instantMarking
        global list2

        list1 = instantMarkingNow.split(", ")
        list2 = []
        for subString in list1:
            if subString == "Y" or subString == "YES":
                list2 = True
            elif subString == "N" or subString == "NO":
                list2 == False
            else:
                print()
                print("Invalid response. Please try again")
                askInstantMarking()
                checkAskInstantMarking()

            instantMarking = list2
        
        print()

    askNumQuestions()
    checkAskNumQuestions()

    askInstantMarking()
    checkAskInstantMarking()
    
    def randpair(dict):
        """Finds a random key-value pair from a dictionary"""
        items = list(dict.items())
        rand = random.randint(0, len(items)-1)
        return items[rand]

    for num in range(1, numQuestions+1): #initialises a smaller random set of countries and capitals
        randPair = randpair(possibleQuestions)
        country = randPair[0]
        capital = randPair[1]

        gameQuestions[country] = capital
        del possibleQuestions[country]
    
    def anyInList(list1, comparable):
        for i in list1:
            if i.upper() == comparable:
                return True
        return False
    



    def remove(list1, comparable):
        for i in list1:
            if i == comparable:
                list1.remove(comparable)
        return list1
    

    #actually ask questions
    num = 0
    global score
    score = 0
    print(gameQuestions.items())

    num+= 1


    global askTrueFalse

    def askTrueFalse(randNum):
        if gameType == "TRUEFALSE" or gameType[0] == "TRUEFALSE" or gameType[1] == "TRUEFALSE" or gameType[2] == "TRUEFALSE": # if true or false gamemode is active
            
            global quality
            quality = "TRUEFALSE"

            if randNum == True: #decides if the answer is true or false
                
                global response

                #asks the question
                response = input(f"Q{num}: Is the capital city of {countries[0]} {capitals[0]}?\n\tOptions: \"true\"/\"t\", \"false\"/\"f\"\n\tEnter here: ").upper()
                if response == "T" or response == "TRUE":
                    print()
                    response == capitals[0] #the player got the question right
                elif response == "F" or response == "FALSE":
                    response = "INCORRECT" #the player got the question wrong
                else:
                    print()
                    print("Invalid response. Please try again")
                    askTrueFalse()

            else:

                #asks the question
                response = input(f"Q{num}: Is the capital city of {countries[0]} {randpair(possibleQuestions)[1][0]}?\n\tOptions: \"true\"/\"t\", \"false\",\"f\"\n\tEnter here: ").upper()
                if response == "F" or response == "FALSE":
                    response == countries[0] #the player got the question right
                else:
                    print()
                    print("Invalid response. Please try again")
                    askTrueFalse()
            
            if anyInList(capitals, response): #check if the player got the question right
                global score
                score+= 1
                if instantMarking == True: #if instant marking is active
                    print(f"Correct answer. Your score now: {score}/{numQuestions}") #TODO: Add highscore and other answers
            else:
                if instantMarking == True: #if instant marking is active
                    print(f"Incorrect answer. Your answer: {response} Correct answer: {countries[0]} Your score: {score}/{numQuestions}") #TODO: Print correct answer

    if not anyInList(gameType, "ENDLESS"): #if endless mode is not active
        for countries, capitals in gameQuestions.items():

            global randNum
            global randChoice

            print(gameType)

            gameTypeCopy = gameType.copy()

            randChoice = random.choice((remove(gameTypeCopy, "ENDLESS")))
            randNum = random.getrandbits(1)
            if randChoice == "TRUEFALSE": #if true false is active
                askTrueFalse(randNum) #do a true/false question
            elif anyInList():
                pass

print("Welcome to the capital city quiz!")
print("\n\
In this quiz you will be quizzed on a random select of countries and their capitals. You will be scored depending on\n\
how hard the questions were and how well you did. The number of points you score for getting a question right is variable\n\
depending on how hard the question is and will show on the question.\n\n\
At the start of a game you can choose how hard you want the game to be, you can also keep the settings of you last game.\n\
Any words in double quotes: \"type me underneath this paragraph\" are the exact words/phrases you can answer when answering a\n\
question (if you are playing multiple choice or when choosing what sort of game you would like).\n\
")
response = input()
if response.upper() == "type me underneath this paragraph":
    print("Good job, you get how to play this game.")

game()