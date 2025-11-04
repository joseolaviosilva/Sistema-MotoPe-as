from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()
    description = models.TextField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MotorcycleCompatibility(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year_start = models.PositiveIntegerField()
    year_end = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.manufacturer} {self.model} ({self.year_start}-{self.year_end})"