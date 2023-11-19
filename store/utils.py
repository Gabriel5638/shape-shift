from decimal import Decimal
from django.db.models import QuerySet

def calculate_cart_total(cart_items):
    if isinstance(cart_items, QuerySet):  
        total = sum(item.price for item in cart_items)
    else:
        total = sum(item.get('price', 0) for item in cart_items)
    return total