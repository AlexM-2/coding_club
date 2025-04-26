people = {
    "jeremy": {"language": "c++", "level": 4},
    "alex": {"language": "python", "level": 3},
    "mary": {"language": "lua", "level": 2}
}

for person in people:
    codingDetails = people[person]
    language = codingDetails["language"]
    level = codingDetails["level"]

    print(f"Person: {person.title()}      Language: {language.title()}      Level: {level}")
    print()