from django.db import models

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

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=product_image_path)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='Men')
    description = models.TextField() 

    def __str__(self):
        return self.name

class BagItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Add any other fields you need

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"