programming_languages = {
    "lucy":"python",
    "josh":"ruby",
    "matilda":"javaScript",
    "matthew":"C"
}
for person in programming_languages:
    print(f"{person.title()}'s top programming language is {programming_languages[person].title()}.")