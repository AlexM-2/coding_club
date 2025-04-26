import random
import time

print("This is the advanced password picker.")
time.sleep(2)
print("You might have used the basic password picker before.")
time.sleep(2)
print("If you have, you will be already be familiar with some aspects of the advanced version.")
time.sleep(2)
print("Anyway, lets generate a password.")
time.sleep(1)
print(" ")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r","s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
specialCharacters = ["!", "@", "€", "£", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", ";", ":", "'", "|", ",", "<", ".", ">", "/", "?", "~", '"']
verySpecialCharacters = ["§", "±", "¡", "¢", "∞", "¶", "•", "ª", "º", "≠", "“", "‘", "…", "æ", "«", "≤", "≥", "œ", "∑", "´", "¥", "¥", "¨", "ø", "π", "å", "ß", "∂", "ƒ", "©", "˙", "Ω", "≈", "ç", "√", "∫","~", "µ", "¬"]
allCharacterTypes = [letters, numbers, specialCharacters, verySpecialCharacters]
someCharacterTypes = [letters, numbers, specialCharacters]
password = ""

while True:
  amiguousCharacters = input("Do you want amiguous characters in your password? (y/n): ")
  if amiguousCharacters == "y" or amiguousCharacters == "Y" or amiguousCharacters == "yes" or amiguousCharacters == "Yes":
    amiguousCharacters = True
    characterNumber = int(input("How many characters would you like in your password?: "))
    print(" ")
    currentCharacters = 0
    if amiguousCharacters:
      while True:
        if currentCharacters == characterNumber:
          break
        else:
          characterType = random.choice(allCharacterTypes)
          character = random.choice(characterType)
          password = f"{password}{character}"
          currentCharacters+= 1
      print("Generating your password...")
      time.sleep(3)
      print(f"Your password is: {password}")
      time.sleep(1)
      print(" ")
      anotherPassword = input("Would you like to generate another password (y/n)?: ")
      if anotherPassword == "n" or anotherPassword == "N" or anotherPassword == "no" or anotherPassword == "No":
        exit()
      elif anotherPassword == "y" or anotherPassword == "Y" or anotherPassword == "yes" or anotherPassword == "Yes":
        print(" ")
        continue
  elif amiguousCharacters == "n" or amiguousCharacters == "N" or amiguousCharacters == "no" or amiguousCharacters == "No":
    amiguousCharacters = False
    characterNumber = int(input("How many characters would you like in your password?: "))
    print(" ")
    currentCharacters = 0
    if not amiguousCharacters:
      while True:
        if currentCharacters == characterNumber:
          break
        else:
          characterType = random.choice(someCharacterTypes)
          character = random.choice(characterType)
          password = f"{password}{character}"
          currentCharacters+= 1
      print("Generating your password...")
      time.sleep(3)
      print(f"Your password is: {password}")
      print(" ")
      anotherPassword = input("Would you like to generate another password (y/n)?: ")
      if anotherPassword == "n" or anotherPassword == "N" or anotherPassword == "no" or anotherPassword == "No":
        exit()
      elif anotherPassword == "y" or anotherPassword == "Y" or anotherPassword == "yes" or anotherPassword == "Yes":
        print(" ")
        continue
  else:
    print("That is not a valid input. Please try again.")
    continue
  print(" ")
  