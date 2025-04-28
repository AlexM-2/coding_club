pending_orders = ["espresso", "latte", "cappuccino", "espresso", "latte", "cappuccino", "espresso", "latte"]
order_list = []
completed_orders = []
served_orders = []

def take_order():
    """Move orders from pending_orders to order_list"""
    order = pending_orders.pop(0)
    order_list.append(order)

def prepare_order():
    """Move orders from order_list to completed_orders"""
    order = order_list.pop(0)
    completed_orders.append(order)