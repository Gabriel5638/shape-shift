from decimal import Decimal

def calculate_cart_total(cart_items):
    total = sum(item.price for item in cart_items)
    return total