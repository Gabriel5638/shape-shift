from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment, Rating
from .models import CartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json 
import stripe
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from store.forms import ContactForm, CommentForm, RatingForm, SizeSelectionForm, ProductQuantityForm
from store.forms import ProductForm
from django.contrib import messages
from decimal import Decimal
from django.core.serializers import serialize
from django.conf import settings
from django.forms.models import model_to_dict
from .utils import calculate_cart_total


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
    return render(request, 'store/category_products.html', {'products': products,"title": "Protein"})


def creatine_products(request):
    products = Product.objects.filter(category="Creatine")
    return render(request, 'store/category_products.html', {
    "products": products, 
    "title": "Creatine"
})


def electrolytes_products(request):
    products = Product.objects.filter(category="Electrolytes")
    return render(request, 'store/electrolytes.html', {'products': products})


def preworkout_products(request):
    products = Product.objects.filter(category="Preworkout")
    return render(request, 'store/preworkout.html', {'products': products})


def postworkout_products(request):
    products = Product.objects.filter(category="Postworkout")
    return render(request, 'store/postworkout.html', {'products': products})



def success_view(request):
    return render(request, 'sucess.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                f"Contact form submission from {name}",
                f"Email: {email}\n\nMessage:\n{message}",
                email,  # From email address
                ['gabrielpuiu213@gmail.com'], 
                fail_silently=False,
            )
            return render(request, 'success.html')  
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    comment_form = CommentForm()
    rating_form = RatingForm()
    size_form = SizeSelectionForm()
    quantity_form = None  # Initialize with None

    if request.method == 'POST':
        if 'comment_form' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.product = product
                new_comment.user = request.user
                new_comment.save()
                return redirect('product_detail', product_id=product_id)
        elif 'rating_form' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid():
                new_rating = rating_form.save(commit=False)
                new_rating.product = product
                new_rating.user = request.user
                new_rating.save()
                return redirect('product_detail', product_id=product_id)
        elif 'size_form' in request.POST:  # Handling size selection form
            size_form = SizeSelectionForm(request.POST)
            if size_form.is_valid():
                selected_size = size_form.cleaned_data['size']

               

                # Redirect to the product detail page or another appropriate page
                return redirect('product_detail', product_id=product_id)
        elif 'quantity_form' in request.POST:  # Handling quantity form
            quantity_form = ProductQuantityForm(request.POST)
            if quantity_form.is_valid():
                # Process the quantity form as needed
                quantity_form.save()
                # Redirect or perform necessary actions
    else:
        # Set a default value if not a POST request
        quantity_form = ProductQuantityForm()

    comments = Comment.objects.filter(product=product)
    ratings = Rating.objects.filter(product=product)

    context = {
        'product': product,
        'size_form': size_form,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'quantity_form': quantity_form,
        'comments': comments,
        'ratings': ratings,
    }
    return render(request, 'product_detail.html', context)


def add_size(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')  # Assuming the product ID is sent via POST
        size = request.POST.get('size')  # Assuming the size is sent via POST
        quantity = int(request.POST.get('quantity', 0))  # Assuming the quantity is sent via POST

        # Retrieve the product instance based on the provided product_id
        product_instance = Product.objects.get(pk=product_id)  # Assuming Product is your product model

        # Add the size and quantity to the ProductQuantity model
        ProductQuantity.add_size(product=product_instance, size=size, quantity=quantity)

        # Redirect to a success page or another appropriate view
        return redirect('success')  # Change 'success' to your desired URL name

    # Handle GET request or any other scenario
    return HttpResponse("Invalid request")


def add_quantity(request, product_id):
    if request.method == 'POST':
        # Fetch the product based on the product_id from the URL
        product = get_object_or_404(Product, pk=product_id)

        # Assuming the quantity data is sent in the POST request, retrieve it
        selected_quantity = request.POST.get('selected_quantity')

        # Validate and process the selected quantity data
        # Here, you can save the selected quantity for the product
        # Example:
        ProductQuantity.objects.create(product=product, quantity=selected_quantity)

        # Redirect to the product detail page or any other appropriate page
        return redirect('product_detail', product_id=product_id)

    # Handle other HTTP methods if needed or provide a default response
    return redirect('product_detail', product_id=product_id) 


@login_required
def add_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.product = product
            new_comment.save()
            messages.success(request, 'Comment added successfully!')
        return redirect('product_detail', product_id=product_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})


@login_required
def add_rating(request, product_id):
    product = get_object_or_404(Product, pk=product_id)  
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.user = request.user
            new_rating.product = product
            
            if 1 <= new_rating.rating <= 10:
                new_rating.save()
                messages.success(request, 'Rating added successfully!')
            else:
                messages.error(request, 'Invalid rating. Please provide a rating between 1 and 10.')
        else:
            messages.error(request, 'Invalid rating. Please provide a rating between 1 and 10.')
    else:
        form = RatingForm()
    return redirect('product_detail', product_id=product_id)


def add_to_cart_view(request, product_id):
    if request.method == 'POST':
        selected_size = request.POST.get('size')
        selected_quantity = int(request.POST.get('quantity', 1))
        product = Product.objects.get(pk=product_id)
        
        if product.availability != 'In stock':
            return HttpResponse("We are sorry, but this item is out of stock. <a href='{}'>Go Back to All Products</a>".format(reverse('all_products')))
        
        product_price = product.price * Decimal(selected_quantity)
        product_image = product.image.url if product.image else None

        if request.user.is_authenticated:
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                product=product,
                size=selected_size,
                defaults={'quantity': selected_quantity, 'image': product_image, 'price': product_price}
            )
            if not created:
                cart_item.quantity += selected_quantity
                cart_item.price += product_price
                cart_item.save()
        else:
            session_cart = request.session.get('cart', {})
            item_key = f'{product_id}_{selected_size}'
            if item_key in session_cart:
                session_cart[item_key]['quantity'] += selected_quantity
                session_cart[item_key]['price'] = float(product_price)
            else:
                session_cart[item_key] = {
                    'product_id': product_id,
                    'size': selected_size,
                    'quantity': selected_quantity,
                    'image': product_image,
                    'price': float(product_price)
                }
            request.session['cart'] = session_cart
            
        return HttpResponseRedirect(reverse('cart'))
    else:
        # Handle other HTTP methods if needed
        pass
    
def product_admin_panel(request):
    products = Product.objects.all()
    return render(request, 'product_admin.html', {'products': products})

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('product_admin_panel')  # Redirect back to the product admin panel

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_admin_panel')  # Redirect back to the product admin panel after successful addition
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def view_cart(request):
    user = request.user

    if user.is_authenticated:
        cart_items = CartItem.objects.filter(user=user)
    else:
        session_cart = request.session.get('cart', {})
        session_product_ids = [value['product_id'] for value in session_cart.values()]
        cart_items = CartItem.objects.filter(product__id__in=session_product_ids)

    context = {
        'cart_items': cart_items,
        # Add other context data as needed
    }

    return render(request, 'cart.html', context)

    # Assuming you've fetched the cart items and created the forms as previously shown

    # Create instances of the forms
    size_form = SizeSelectionForm()
    quantity_form = ProductQuantityForm()

    context = {
        'cart_items': cart_items,
        'size_form': size_form,
        'quantity_form': quantity_form
    }

    return render(request, 'cart.html', context)

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    
    # Save the price of the item about to be deleted
    item_price = cart_item.price

    # Remove the item from the cart
    cart_item.delete()

    # Recalculate the total price after deletion
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
    else:
        session_cart = request.session.get('cart', {})
        # Fetch and update the cart items
        cart_items = []  # Update this list according to your session structure
        
    total_price = calculate_cart_total(cart_items)

    # Redirect back to the cart page with the updated total price or any other appropriate page
    return redirect('cart')


stripe.api_key = settings.STRIPE_SECRET_KEY

def create_payment_intent(request):
    if request.method == 'POST':
        amount = 1000  # Amount in cents
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
            )
            return JsonResponse({'clientSecret': intent.client_secret})
        except stripe.error.CardError as e:
            return JsonResponse({'error': str(e)})