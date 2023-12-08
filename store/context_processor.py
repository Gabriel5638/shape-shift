from .models import CartItem, Product
from .utils import calculate_cart_total  
from decimal import Decimal


def cart_contents(request):
    user = request.user
    if user.is_authenticated:
        cart_items = CartItem.objects.filter(user=user)
    else:
        session_cart = request.session.get('cart', {})
        cart_items = []
        for key, value in session_cart.items():
            product_id = value['product_id']
            product = Product.objects.get(pk=product_id)

            cart_item = {
                'product': {
                    'name': product.name,
                    'description': product.description,
                    # Add other necessary details
                },
                'size': value['size'],
                'quantity': value['quantity'],
                'image': value['image'],
                'price': value['price']
            }
            cart_items.append(cart_item)

    # Calculate the total price based on the updated cart items after deletion
    total_price = calculate_cart_total(cart_items)

    # Calculate the grand total by adding any additional costs or discounts
    additional_costs_or_discounts = 0  # Replace with your logic
    grand_total = total_price + additional_costs_or_discounts

    # Convert the Decimal values to float before returning
    total_price = float(total_price)
    grand_total = float(grand_total)
    
    return {
        'cart_items': cart_items,
        'total_price': total_price,
        'grand_total': grand_total
    }
