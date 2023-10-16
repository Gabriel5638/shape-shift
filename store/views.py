from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib import messages
from django.db.models import Q

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('all_products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'store/all_products.html', context)


def women_products(request):
    products = Product.objects.filter(category='Women')
    return render(request, 'clothes/women.html', {'products': products})

def men_product_list(request):  
    products = Product.objects.filter(category='Men')  
    return render(request, 'clothes/men.html', {'products': products})

def product_detail(request, product_id):
    # Retrieve the product based on the provided product_id
    product = get_object_or_404(Product, pk=product_id)

    # Example additional logic:
    # You can add logic to display related products.

    # For example, retrieve related products based on the product's category
    related_products = Product.objects.filter(category=product.category).exclude(pk=product_id)[:3]

    #  add more logic here as needed, such as displaying reviews, calculating discounts, etc.

    # Return the rendered template with the context data
    return render(request, 'store/product_detail.html', {'product': product, 'related_products': related_products})