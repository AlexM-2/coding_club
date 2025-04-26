print("\n============================== Challenge 1: Make Shirt ==============================================\n")

def makeShirt(message, size):
    print(f"This shirt is {size["waist"]} around the waist and {size["height"]} tall.\nIt has \"{message["message"]}\" with the font {message["font"]} printed on the front.")

makeShirt({"message":"I love C++.", "font":"comic sans"}, {"waist":"30cm", "height":"40cm"})

print()

def makeShirt(message = {"message":"I love Python.", "font": "arial"}, size = {"waist":"29cm", "height":"37cm"}):
    print(f"This shirt is {size["waist"]} around the waist and {size["height"]} tall.\nIt has \"{message["message"]}\" with the font {message["font"]} printed on the front.")

makeShirt()

print(f"\n{"="*100}\n")