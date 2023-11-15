from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.db.models import Q
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
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



def contact_form(request):
    return render(request, 'contact_form.html')


def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # You can customize this email content as needed
        email_content = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Replace the following with your email sending logic
        send_mail(
            'New Contact Form Submission',
            email_content,
            'your@example.com',  # Replace with your email address
            ['recipient@example.com'],  # Replace with the recipient's email address
            fail_silently=False,
        )

        # Add success message
        messages.success(request, 'Your message was successfully submitted!')

        # Redirect after successful submission
        return HttpResponseRedirect(reverse('contact_form'))

    # Handle GET requests or other cases
    return HttpResponseRedirect(reverse('contact_form'))

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

