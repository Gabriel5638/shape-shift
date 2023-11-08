from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib import messages
from django.db.models import Q
#from .forms import CommentForm make comment form#

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # Start with the default queryset of all products
    products = Product.objects.all()

    # Define default sorting options
    sort = request.GET.get('sort', 'name')  # Default to sorting by name
    direction = request.GET.get('direction', 'asc')  # Default to ascending order

    # Handle sorting based on user input
    if sort == 'name':
        field_to_sort = 'name'
    elif sort == '-name':
        field_to_sort = '-name'  # Adjust the value to match the HTML
    elif sort == 'price':
        field_to_sort = 'price'
    elif sort == '-price':
        field_to_sort = '-price'  # Adjust the value to match the HTML
    else:
        field_to_sort = 'name'  # Default to sorting by name

    # Apply sorting direction
    if direction == 'desc':
        field_to_sort = '-' + field_to_sort  # Add '-' for descending order

    # Apply sorting to the queryset
    products = products.order_by(field_to_sort)

    # Handle search queries
    query = request.GET.get('q', None)
    if query:
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'sort': sort,
        'direction': direction,
    }

    return render(request, 'store/all_products.html', context)


def women_products(request):
    products = Product.objects.filter(category='Women')
    return render(request, 'clothes/women.html', {'products': products})


def men_product_list(request):  
    products = Product.objects.filter(category='Men')  
    return render(request, 'clothes/men.html', {'products': products})


def keychain_products(request):
    products = Product.objects.filter(category="Keychains")
    return render(request, 'store/keychains.html', {'products': products})


def wriststraps_products(request):
    products = Product.objects.filter(category="Wriststraps")
    return render(request, 'store/wriststraps.html', {'products': products})


def yogamats_products(request):
    products = Product.objects.filter(category="Yogamats")
    return render(request, 'store/yogamats.html', {'products': products})


def foamrollers_products(request):
    products = Product.objects.filter(category="Foamrollers")
    return render(request, 'store/foamrollers.html', {'products': products})


def protein_products(request):
    products = Product.objects.filter(category="Protein")
    return render(request, 'store/protein.html', {'products': products})


def creatine_products(request):
    products = Product.objects.filter(category="Creatine")
    return render(request, 'store/creatine.html', {'products': products})


def electrolytes_products(request):
    products = Product.objects.filter(category="Electrolytes")
    return render(request, 'store/electrolytes.html', {'products': products})


def preworkout_products(request):
    products = Product.objects.filter(category="Preworkout")
    return render(request, 'store/preworkout.html', {'products': products})


def postworkout_products(request):
    products = Product.objects.filter(category="Postworkout")
    return render(request, 'store/postworkout.html', {'products': products})


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

def add_to_bag(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        quantity = int(request.POST.get('quantity'))

        if quantity > 0:
            bag = request.session.get('bag', {})
            bag_item = bag.get(product_id, 0)
            bag[product_id] = bag_item + quantity
            request.session['bag'] = bag
            return redirect(request.META.get('HTTP_REFERER'))

    return HttpResponseBadRequest("Invalid request")

def view_bag(request):
    # Retrieve bag items from the session
    bag = request.session.get('bag', {})

    # Create a list of bag items with product details
    bag_items = []
    total = 0

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        total += product.price * quantity
        bag_items.append({
            'product': product,
            'quantity': quantity,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
    }

    return render(request, 'store/bag.html', context)