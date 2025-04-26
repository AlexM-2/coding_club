from time import ctime # ctime() gets the current time since the epoch in a readable format

productInventory = { #initialise data
    1: {"name": "tomatoes;1.1", "quantity": 12, "price": 0.2, "category": "fruits&Veg"},
    2: {"name": "carrots;0.8", "quantity": 7, "price": 0.6, "category": "fruits&Veg"},
    3: {"name": "cucumbers;0.9", "quantity": 6, "price": 0.7, "category": "fruits&Veg"},
    4: {"name": "vaccumCleaner;1.5", "quantity": 2, "price": 500, "category": "houseAppliances"},
    5: {"name": "schoolChair;0.5", "quantity": 50, "price": 10, "category": "furniture"}
}

#==============================================defining functions=======================================================================

def money(number): #converts a decimal into a formatted money string eg 0.5 -> "50p", 500 -> "£500.00"
    if number.is_integer() == True:
        return f"£{int(number)}.00"
    elif number < 1:
        return f"{int(number*100)}p"
    elif (number*10).is_integer() == True:
        return f"£{number}0"

def readableTime(): #converts ctime() into a formatted string
    cTime = ctime()# -> "day mon dm xx:yy:zz year"

    readable_time = "" # initialise string

    day = cTime[0]+cTime[1]+cTime[2]
    month = cTime[4]+cTime[5]+cTime[6]
    dayMonth = cTime[8]+cTime[9]
    time = cTime[11]+cTime[12]+cTime[13]+cTime[14]+cTime[15]+cTime[16]+cTime[17]+cTime[18]
    year = cTime[20]+cTime[21]+cTime[22]+cTime[23]
    
    if day == "Mon": #formats the day of the week
        readable_time = "Monday"
    elif day == "Tue":
        readable_time = "Tuesday"
    elif day == "Wed":
        readable_time = "Wednesday"
    elif day == "Thu":
        readable_time = "Thursday"
    elif day == "Fri":
        readable_time = "Friday"
    elif day == "Sat":
        readable_time = "Saturday"
    elif day == "Sun":
        readable_time = "Sunday"
    
    if not dayMonth[0] == " " and not dayMonth[0] == "1": #formats the day of the month
        if dayMonth[1] == "1":
            readable_time = readable_time + f" {dayMonth[0]}1st"
        elif dayMonth[1] == "2":
            readable_time = readable_time + f" {dayMonth[0]}2nd"
        elif dayMonth[1] == "3":
            readable_time = readable_time + f" {dayMonth[0]}3rd"
        else:
            readable_time = readable_time + f" {dayMonth[0]}{dayMonth[1]}th"
    elif dayMonth[0] == " ":
        if dayMonth[1] == "1":
            readable_time = readable_time + " 1st"
        elif dayMonth[1] == "2":
            readable_time = readable_time + " 2nd"
        elif dayMonth[1] == "3":
            readable_time = readable_time + " 3rd"
        else:
            readable_time = readable_time + f" {cTime[1]}th"
    
    if month == "Jan": #formats the month
        readable_time = readable_time + " January"
    elif month == "Feb":
        readable_time = readable_time + " February"
    elif month == "Mar":
        readable_time = readable_time + " March"
    elif month == "Apr":
        readable_time = readable_time + " April"
    elif month == "May":
        readable_time = readable_time + " May"
    elif month == "Jun":
        readable_time = readable_time + " June"
    elif month == "Jul":
        readable_time = readable_time + " July"
    elif month == "Aug":
        readable_time = readable_time + " August"
    elif month == "Sep":
        readable_time = readable_time + " September"
    elif month == "Oct":
        readable_time = readable_time + " October"
    elif month == "Nov":
        readable_time = readable_time + " November"
    elif month == "Dec":
        readable_time = readable_time + " December"
    
    #adds the year and time to readable_time
    readable_time = readable_time + " " + year
    readable_time = readable_time + " " + time
    
    return readable_time

def enterQuantity():
        inputQuantity = input("Enter the desired quantity of the product: ")
        if not inputQuantity.isdigit():
            print("Invalid entry. Please try again.")
            enterQuantity()
        return int(inputQuantity)
    
def enterPrice():
    inputPrice = input("Enter the price of the product eg. 0.2, 12: ")
    if inputPrice.replace(".", "", 1).isdigit(): #if inputPrice is a float
        if (float(inputPrice)*100).is_integer():
            return float(inputPrice)
        else:
            print("Invalid entry. Please try again.")
            enterPrice()
    elif inputPrice.isdigit():
        return int(inputPrice)
    else:
        print("Invalid entry. Please try again.")
        enterPrice()

def printInventory(): #prints the product inventory as a table, changing the space between the different elements depending on the length of the string

    #initialise length of string lists
    listID = []
    listName = []
    listQuantity = []
    listPrice = []
    listCategory = []
    
    for productID, productInfo in productInventory.items(): #loops through productInventory and appends the length of the strings to the lists
        
        listID.append(  len(   f"ID: {productID}"   )  )
        listName.append(  len(   f"Name: {productInfo["name"]}"   )  )
        listQuantity.append(  len(   f"Quantity: {productInfo["quantity"]}"   )  )
        listPrice.append(  len(   f"Price: {money(productInfo["price"])}"   )  )
        listCategory.append(  len(   f"Price: {productInfo["category"]}"   )  )
    
    #finds the longest length string and adds 5
    maxCharLenID = max(listID) + 5
    maxCharLenName = max(listName) + 5
    maxCharLenQuantity = max(listQuantity) + 5
    maxCharLenPrice = max(listPrice) + 5
    maxCharLenCategory = max(listCategory) + 5

    for productID, productInfo in productInventory.items(): #actually prints the table (productInventory)

        #finds the number of " " needed so all the elements in a collumn are parallel using the maxCharLen variables
        spaceID = complete(maxCharLenID - (len(f"ID: {productID}")))
        spaceName = complete((   maxCharLenName-(len(f"Name: {productInfo["name"]}"))   ) )
        spaceQuantity = complete((   maxCharLenQuantity-(len(f"Quantity: {productInfo["quantity"]}"))   ) )
        spacePrice = complete((   maxCharLenPrice-(len(f"Price: {money(productInfo["price"])}"))   ) )
        spaceCategory = complete((   maxCharLenCategory-(len(f"Category: {productInfo["category"]}"))   ) )

        #actually actually prints the table
        print()
        print(f"|{spaceID[0]}ID: {productID}{spaceID[1]}|{spaceName[0]}Name: {productInfo["name"]}{spaceName[1]}|{spaceQuantity[0]}Quantity: {productInfo["quantity"]}{spaceQuantity[1]}|{spacePrice[0]}Price: {money(productInfo["price"])}{spacePrice[1]}|{spaceCategory[0]}Category: {productInfo["category"]}{spaceCategory[1]}|")
    print()

def complete(num):
    # print((num/2)+0.5)
    # print((num/2)-0.5)
    n = num/2
    if num % 2 == 0:
        return [" " * int(n), " " * int(n)]
    else:
        return [" " * int(n-0.5), " " * int(n+0.5)]

def addProduct():

    response = input("There is a shortage in demand. Would you like to add another product? (y/n): ")

    if response.upper() == "Y" or response.upper() == "YES":

        inputName = input("Enter the name for the product: ")
        inputCategory = input("Enter the category of the product: ")

        productInventory[max(productInventory)+1] = {"name": inputName, "quantity": enterQuantity(), "price": enterPrice(), "category": inputCategory}
    print(f"Here is the updated product inventory (if any updates) of Sahara Industries as of {readableTime()}")
    printInventory()

def changePrice(product):

    response = input(f"There is too much demand of {product}! Would you like to change the price? (y/n): ")

    if response.upper() == "Y" or response.upper() == "YES":
        productInventory[findID(product)]["price"] = enterPrice()
    print(f"Here is the updated product inventory (if any updates) of Sahara Industries as of {readableTime()}")
    printInventory()
    
def findID(name):
    for id, info in productInventory.items():
        if info["name"] == name:
            return id

def deleteProduct(product):
    del productInventory[findID(product)]
    print(f"There is no one buying {product}, we have decided to stop selling them.")
    print(f"Here is the updated product inventory (if any updates) of Sahara Industries as of {readableTime()}")
    printInventory()

#=======================================executing code===========================================

#looping through the products and printing them in the readable format
print(f"Here is the product inventory of Sahara Industries as of {readableTime()}")
printInventory()

#adding two more products and updating the product list
addProduct()
addProduct()

#chaninging the price of two products
changePrice("vaccumCleaner;1.5")
changePrice("cucumbers;0.9")

#deleting a product and printing the updated product inventory
deleteProduct("schoolChair;0.5")