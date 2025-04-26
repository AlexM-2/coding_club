productInventory = { #data
    1: {"name": "tomatoes;1.1", "quantity": 12, "price": 0.2, "category": "fruits&Veg"},
    2: {"name": "carrots;0.8", "quantity": 7, "price": 0.6, "category": "fruits&Veg"},
    3: {"name": "cucumbers;0.9", "quantity": 6, "price": 0.7, "category": "fruits&Veg"},
    4: {"name": "vaccumCleaner;1.5", "quantity": 2, "price": 500, "category": "houseAppliances"},
    5: {"name": "schoolChair;0.5", "quantity": 50, "price": 10, "category": "furniture"}
}
def printInventory():

    print("="*50)
    print()
    for productID, productInfo in productInventory.items(): # loops through each product in productInventory
        
        #prints the id and productInfo of the product
        print(f"ID: {productID}, Name: {productInfo["name"]}, Quantity: {productInfo["quantity"]}, Price: {productInfo["price"]}, Category: {productInfo["category"]}")

printInventory()

productInventory[6] = {"name": "car;1.3", "quantity": 10, "price": 300000, "category": "veichles"}
productInventory[7] = {"name": "diningTable;1", "quantity": 5, "price": 600, "category": "furniture"}

productInventory[4]["price"] = 600
productInventory[3]["price"] = 0.8

del productInventory[5]

print("\nHere is the updated product inventory:\n")
printInventory()