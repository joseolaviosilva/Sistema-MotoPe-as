from django.db import models
from customers.models import Customer
from inventory.models import Supplier

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type.capitalize()} - {self.amount} on {self.date}"

class Debt(models.Model):
    DEBT_TYPES = [
        ('payable', 'Payable'),
        ('receivable', 'Receivable'),
    ]
    type = models.CharField(max_length=10, choices=DEBT_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"Debt of {self.amount} due on {self.due_date}"