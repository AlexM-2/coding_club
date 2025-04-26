def moneyFormat(num):
    if num < 0:
        return
    elif num < 1:
        return f"{int(num*100)}p"
    elif num % 1 == 0:
        return f"£{num}0"
    
    

def calculateVat(price, vat = 0.2):
    price = float(price)
    vat = float(vat)
    return [price, price*vat, price + price*vat]

print("Welcome to the VAT calculator!")

price = input("What is the price of the product?: ")
vat = input("What is the VAT in your country/area?: ")

print()

vatList = calculateVat(price, vat)
print(f"The total price of the product including VAT is {moneyFormat(vatList[2])}. The price without VAT is {moneyFormat(vatList[0])}. The price added on to the product due to VAT is {moneyFormat(vatList[1])}.")