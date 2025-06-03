# import random

#e short for espresso, l short for latte, c short for cappucino
POSSIBLE_ORDERS: set[str] = {"espresso","e", "latte","l", "cappuccino","c"}
POSSIBLE_SIDES: set[str] = {"biscuit","b", "milk","m" "cake","c"}

pending_orders = []
order_list = []
completed_orders = []
served_orders = []
washing_up_list = []

class Order(str):

    def __new__(cls, order_type: str, *sides: str):

        order_type = order_type.lower()

        if not order_type in POSSIBLE_ORDERS:
            raise ValueError("Argument parsed not a known coffee type")
        
        return super().__new__(cls, order_type)

    def __init__(self, order_type: str, *sides: str):

        super().__init__(order_type)



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