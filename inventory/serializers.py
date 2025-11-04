from rest_framework import serializers
from .models import Product, Supplier, MotorcycleCompatibility

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class MotorcycleCompatibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = MotorcycleCompatibility
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'