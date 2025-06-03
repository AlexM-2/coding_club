while quit:
    num1 = input("What is the first number to multiply? (enter q to quit): ")
    if num1.upper() == "Q":
        print(f"\n{"="*100}\n")
        quit()

    num2 = input("What is the second number to multiply? (enter q to quit): ")
    if num2.upper() == "Q":
        print(f"\n{"="*100}\n")
        quit()

    product = int(num1) * int(num2)
    print(f"The product of the first number, {num1}, multiplied by the second one, {num2}, is {product}.")

    print()