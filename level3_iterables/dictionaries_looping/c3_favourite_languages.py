names = ["Joe", "Joseph", "Oliver", "Jeff", "Jeffrey", "personName", "Jeremy", "Jake", "Jamie", "James", "Alex", "Matt", "Matthew"]
poll_data = {
    "Joe": "C",
    "Joseph": "C+",
    "Jeff": "C++",
    "Jeffrey": "C*",
    "Jeremy": "C#",
    "Jake": "C--",
    "Jamie": "Objective-C",
    "James": "Split-C",
    "Alex": "Python",
    "Matt": "Scala",
    "Matthew": "Java"
}

for name in names:
    
    if name in poll_data:
        print(f"Thank you, {name} for taking part in our survey!")
    else:
        input(f"{name}, would you like to take part in our survey?: ")
        print("Thank you for your response!")