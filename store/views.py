from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'clothes/women.html', {'products': products})

def product_detail(request, product_id):
    # Retrieve the product based on the provided product_id
    product = get_object_or_404(Product, pk=product_id)

    # Example additional logic:
    # You can add logic to display related products.

    # For example, retrieve related products based on the product's category
    related_products = Product.objects.filter(category=product.category).exclude(pk=product_id)[:3]

    # You can add more logic here as needed, such as displaying reviews, calculating discounts, etc.

    # Return the rendered template with the context data
    return render(request, 'store/product_detail.html', {'product': product, 'related_products': related_products})