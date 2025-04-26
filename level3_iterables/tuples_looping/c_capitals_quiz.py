import random

score = 0

countryCapitals = [
    ("England", "London"),
    ("France", "Paris"),
    ("Italy", "Rome"),
    ("Spain", "Madrid"),
    ("United States", "Washington DC")
]

for country, capital in countryCapitals:
    print(f"What is the capital of {country}?")
    answer = input()
    if answer.lower() == capital.lower():
        print("Correct!")
        score+= 1
    else:
        print("Incorrect.")
print()
print("Your score:", score)