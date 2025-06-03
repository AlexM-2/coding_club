def printAddress():
    print("Mary Rose")
    print("21")
    print("Princess Road")
    print("Hackney")
    print("London")
    print("E2 8AB")

printAddress()
print()
printAddress()
print()
printAddress()

print(f"\n{"="*25}\n")

def printAddress(name):
    print(name)
    print("21")
    print("Princess Road")
    print("Hackney")
    print("London")
    print("E2 8AB")

printAddress("Mary Rose")
print()
printAddress("Mr Sir")
print()
printAddress("Jane Doe")

print(f"\n{"="*25}\n")

def printAddress(name, streetNumber):
    print(name)
    print(streetNumber)
    print("Princess Road")
    print("Hackney")
    print("London")
    print("E2 8AB")

printAddress("Mary Rose", 21)
print()
printAddress("Mr Sir", 69)
print()
printAddress("Jane Doe", 5)

print(f"\n{"="*25}\n")

def printAddress(name, streetNumber, postcode):
    print(name)
    print(streetNumber)
    print("Princess Road")
    print("Hackney")
    print("London")
    print(postcode)

printAddress("Mary Rose", 21, "E2 8AB")
print()
printAddress("Mr Sir", 69, "H8 8LL")
print()
printAddress("Jane Doe", 5, "BS17 5HM")

print(f"\n{"="*25}\n")

def printAddress(name, streetNumber, postcode = "E2 8AB"):
    print(name)
    print(streetNumber)
    
    print("Princess Road")
    print("Hackney")
    print("London")
    print(postcode)

printAddress("Mary Rose", 21, "E2 8AB")
print()
printAddress("Mr Sir", 69)
print()
printAddress("Jane Doe", 5, "BS17 5HM")

print(f"\n{"="*50}\n")

def formatName(firstName, lastName):
    return f"{firstName} {lastName}".title()

artist = formatName("lewis", "capaldi")
print(artist)

print(f"\n{"="*50}\n")

def calculateVat(price, VAT = 0.2):
    return price + (price*VAT)

nintendoConsolePrice = calculateVat(220)
marioGamePrice = calculateVat(60)

print(f"It costs £{nintendoConsolePrice} to buy a nintendo switch (including VAT).")
print(f"It costs £{marioGamePrice} to buy a mario game (including VAT).")