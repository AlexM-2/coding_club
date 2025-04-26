print()
print("=========================================== Challenge 5 ===========================================")
print()

vowels = 0

string = list(input("Enter a string: "))
for character in string:
   if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
      vowels+= 1
print(f"There are {vowels} vowel(s) in the string.")

print()
print("="*100)
print()