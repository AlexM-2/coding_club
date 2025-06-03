def print_new_section():
    print(">"*20)

def greet_users(names: list[str]):
    """Greets every name in names"""
    for user in names:
        print(f"Hello, {user.title()}!")

usernames = ["Rob", "Robert", "Robby"]
greet_users(usernames)

print_new_section()

unprinted_designs: list = ["Spaceship", "Flower", "Scizzors"]
printed_models: list = []

def print_single_design(design):
    """Prints a design"""
    print(f"Printing design: {design}.")
    #would probably utilise api call from real life 3D printer if this were to be used in a real world context

def print_designs(designs):
    """Prints every design in a list using print_design function"""
    for design in designs:
        print_single_design(design)
        unprinted_designs.pop(unprinted_designs.index(design))
        printed_models.append(design)

def show_completed_designs():
    print("Completed models:")
    for model in printed_models:
        print(f"\t{model}")

print_designs(unprinted_designs)
show_completed_designs()

print_new_section()