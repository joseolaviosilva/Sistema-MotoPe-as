from django.db import models
from customers.models import Customer
from inventory.models import Product
from human_resources.models import Employee

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    sale_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Sale #{self.id} to {self.customer.name}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Sale #{self.sale.id}"

    def save(self, *args, **kwargs):
        # Update the total amount of the sale when a sale item is saved
        super().save(*args, **kwargs)
        self.sale.total_amount = sum(item.unit_price * item.quantity for item in self.sale.items.all())
        self.sale.save()