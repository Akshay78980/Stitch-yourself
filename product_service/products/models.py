from django.db import models
import uuid


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True, help_text="Enter category name (e.g., Hoodie, T-Shirt)")

    def __str__(self) -> str:
        return self.name
    
class Brand(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    product_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    group_sku_number = models.CharField(max_length = 20, unique=True)
    name = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.name} ({self.group_sku_number})'
    
    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]
    


class ProductVariant(models.Model):

    SIZES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    color = models.CharField(max_length=50, null=True, blank=True, db_index=True)
    size = models.CharField(max_length=20, choices=SIZES, null=True, blank=True, db_index=True)
    quantity = models.PositiveIntegerField()
    variant_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, db_index=True)
    image1 = models.ImageField(upload_to='product_images/')
    image2 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='product_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='product_images/', null=True, blank=True)

    class Meta:
        unique_together = ['product','color','size']
        indexes = [
            models.Index(fields=['color'])
        ]

    def __str__(self):
        return f'{self.product.__str__()} - {self.color}'

