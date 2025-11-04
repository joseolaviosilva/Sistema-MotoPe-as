from django_filters import rest_framework as filters
from .models import Product, Supplier, MotorcycleCompatibility

class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
            'sku': ['exact'],
            'supplier__name': ['icontains'],
        }

class SupplierFilter(filters.FilterSet):
    class Meta:
        model = Supplier
        fields = {
            'name': ['icontains'],
        }

class MotorcycleCompatibilityFilter(filters.FilterSet):
    class Meta:
        model = MotorcycleCompatibility
        fields = {
            'manufacturer': ['icontains'],
            'model': ['icontains'],
            'year_start': ['gte'],
            'year_end': ['lte'],
        }
