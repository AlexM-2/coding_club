# import random

#e short for espresso, l short for latte, c short for cappucino
POSSIBLE_ORDERS: set[str] = {"espresso","e", "latte","l", "cappuccino","c"}
POSSIBLE_SIDES: set[str] = {"biscuit","b", "milk","m" "cake","c"}

ALL_TABLES: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}

pending_orders = []
order_list = []
completed_orders = []
served_orders = []
washing_up_list = []

class Order(str):

    def __new__(cls, order_type: str, *sides: str):

        order_type = order_type.lower()

        if not order_type in POSSIBLE_ORDERS:
            raise ValueError("Argument (coffee type) parsed to Order creation is not on the menu of this coffee shop.")
        
        return super().__new__(cls, order_type)

    def __init__(self, order_type: str, table: int, *sides: str):

        super().__init__(order_type)

        if not table in ALL_TABLES:
            raise ValueError("This table does not exist the coffee shop")
        self.table = table

        for index, side in enumerate(sides):
            if side in POSSIBLE_SIDES:
                setattr(self, f"side{index+1}")
            else:
                raise ValueError("Argument (side) parsed to Order creation is not on the menu of this coffee shop.")
            

def take_order():
    """Take a customer's order"""
    order = pending_orders.pop(0)
    order_list.append(order)

def prepare_order():
    """Cook the customer's order"""
    order = order_list.pop(0)
    completed_orders.append(order)

def serve_order():
    """Serve the customer's order"""
    order = completed_orders.pop(0)
    served_orders.append(order)

def clean_table():
    """Bring the dirty cups and dishes from the table to the kitchen and clean the table"""
    washing_up = served_orders.pop(0)
    washing_up_list.append(washing_up)

def wash_up():
    """Wash up dirty cups and dishes"""
    washing_up_list.pop(0)


time = 0
while True:
    time+=1
