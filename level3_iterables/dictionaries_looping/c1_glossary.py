# glossary = {
#     "data types": {
#         "Integer": "A non decimal/fraction number that you can use as an index, key or other use that requires an integer.",
#         "String": "A string is any set of characters in an order.",
#         "List": "A list of items eg. myList = [\"Hello World!\", variable, otherList, 6, tuple] A list can include any other data type inside it. The items in a list can be accessed with an index based on the position of an item in it.",
#         "Dictionary": "A dictionary is like a list but instead of having an index, a dictionary has a key, which can be any data type. This means you can't access items in it based on the position in the dictionary it is in. They also have curly brackets ( {} ) rather than square brackets ( [] )"
#     },
#     "loops": {
#         "While loop": "buiv ewvue",
#         "For loop": "vneoir"
#     },
#     "blahs": {
#         "blahblah":"blahblahblah",
#         "blAH":"blAHblAHblAHblAHblAHblAH"
#     }
# }

glossary = {
    
    "Integer": "A non decimal/fraction number that you can use as an index, key or other use that requires an integer.",
    "String": "A string is any set of characters in an order.",
    "List": "A list of items eg. myList = [\"Hello World!\", variable, otherList, 6, tuple] A list can include any other data type inside it. The items in a list can be accessed with an index based on the position of an item in it.",
    "Dictionary": "A dictionary is like a list but instead of having an index, a dictionary has a key, which can be any data type. This means you can't access items in it based on the position in the dictionary it is in. They also have curly brackets ( {} ) rather than square brackets ( [] )",
    "While loop": "A loop that will run and continue running on a condition eg while n > 10: ; print(\"blahblah\")",
    "For loop": "A loop that runs for every item in a list, tuple, or dictionary. Has a local variable that is the value in the iterable the for loop is currently checking eg people = ['joseph', 'joe', 'jeff'] ; for person in people: ; print(person.title())" 
}

for word, meaning in glossary.items():
    print()
    print(f"{word} = {meaning}")