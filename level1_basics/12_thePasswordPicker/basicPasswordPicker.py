#===========: The Basic Password Picker :===========#

import random
import string
import time

print("Welcome to The Password Generator!")
time.sleep(1)
print()

#possible words for password
nouns = ["time", "year", "people", "way", "day", "man", "thing", "woman", "life", "child", "world", "school", "state", "family", "student", "group", "country", "problem", "hand", "part", "place", "case", "week", "company", "system", "program", "question", "work", "government", "number", "night", "point", "home", "water","room", "mother", "area", "money", "story", "fact", "month", "lot"]

adjectives = ["red", "big", "tasty", "small", "round", "long", "great","young", "hot", "cold", "dark", "new", "first", "last", "old", "right", "wrong", "big", "small", "round", "long", "great", "young", "hot", "cold", "dark", "new", "first", "last", "old", "right", "wrong", "round", "long", "great", "young", "hot", "cold", "dark", "new", "first", "last", "old"]

adminPassword = "VerySecurePassword"

while True:
  #password
  noun = random.choice(nouns)
  specialCharacter = random.choice(string.punctuation)
  adjective = random.choice(adjectives)
  number = random.randrange(0, 100)
  password = f"{noun}{specialCharacter}{adjective}{number}"

  #print password
  print("Generating password...")
  time.sleep(2)
  print(f"Your password is: {password}")
  time.sleep(1)
  print()

  #another password
  anotherPassword = input("Would you like to generate another password (y/n)?: ")
  if anotherPassword == "n" or anotherPassword == "N" or anotherPassword == "no" or anotherPassword == "No":

    adminPasswordAttempt = input("Enter admin password to change nouns or adjectives. Enter 'q' to stop the program: ")
    print()

    if adminPasswordAttempt == adminPassword:

      while True:
        changeWhat = input("Would you like to change nouns or adjectives (n/a)?: ")
        if changeWhat == "n" or changeWhat == "N":
          nouns.append(input("Enter a noun to add to the list: "))
          print()
          print(f"The new list of nouns is: {nouns}")
          print()
        elif changeWhat == "a" or changeWhat == "A":
          adjectives.append(input("Enter an adjective to add to the list: "))
          print()
          print(f"The new list of adjectives is: {adjectives}")
          print()
        exit = input("Would you like to change another list (y/n)?: ")
        if exit == "n" or exit == "N":
          break
          
    elif adminPasswordAttempt == "q" or adminPasswordAttempt == "Q":
      print("="*100)
      print()
      break
    else:
      print("Incorrect password. Exiting...")
      break