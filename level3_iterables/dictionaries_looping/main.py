person = {
    "First name": "Mary",
    "Last name":"Jones",
    "Age":20,
    "City":"Bristol"
}
for key, value in person.items(): # "too many values to unpack"
    print(f"{key}: {value}")

print()

books = {
    "Harry Potter": "JK Rowling",
    "The BFG": "Roald Dahl",
    "Charlotte's Web": "Jackeline Wilson"
}
for book, author in books.items():
    print(f"{book.title()} was written by {author.title()}.")

print()

phone_directory = {
    "josh": 7656987654,
    "mary": 7654987654,
    "lucy": 7987654321
}
for person, number in phone_directory.items():
    print(f"{person.title()} has phone number 0{number}.")

print()

capitals = {
    "France": "Paris",
    "Japan": "Tokyo",
    "Brazil": "Brazília",
    "Canada": "Ottowa",
    "India": "New Delhi"
}
for country in capitals:
    print(f"The capital of {country} is {capitals[country]}.")