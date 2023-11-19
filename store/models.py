from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

def product_image_path(instance, filename):
    return f'products/{instance.category.lower()}/{filename}'

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Men', 'Men'),
        ('Women', 'Women'),
        ('Keychains', 'Keychains'),
        ('Wriststraps', 'Wriststraps'),
        ('Yogamats', 'Yogamats'),
        ('Foamrollers', 'Foamrollers'),
        ('Protein', 'Protein'),
        ('Creatine', 'Creatine'),
        ('Electrolytes', 'Electrolytes'),
        ('Preworkout', 'Preworkout'),
        ('Postworkout', 'Postworkout'),
    ]

    SIZE_CHOICES = [
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=product_image_path)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='Men')
    description = models.TextField()
    size = models.CharField(max_length=50, choices=SIZE_CHOICES, blank=True, null=True)

    def __str__(self):  
        return self.name
    
class ProductQuantity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50, choices=Product.SIZE_CHOICES)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'size',)
    

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        unique_together = ('user', 'product', 'size',)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # You can include additional fields like 'edited_at' or 'parent_comment' for replies

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    
    # Updated rating field with validators
    rating = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(1, message='Rating should be greater than or equal to 1.'),
            MaxValueValidator(10, message='Rating should be less than or equal to 10.')
        ]
    )