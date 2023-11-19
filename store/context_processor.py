from .models import CartItem, Product
from .utils import calculate_cart_total  
from decimal import Decimal

def cart_total(request):
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

    # Convert the Decimal to a float before passing it to the context
    total_price = float(total_price)
    
    return {'total_price': total_price}