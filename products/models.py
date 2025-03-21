from django.db import models
from shops.models import Shop

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    calories_per_100g = models.PositiveIntegerField(help_text="Calories per 100g of the product")
    outlet = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')  # Link to the outlet (shop)
    stock = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name