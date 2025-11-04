from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product, Supplier, MotorcycleCompatibility
from .serializers import ProductSerializer, SupplierSerializer, MotorcycleCompatibilitySerializer
from .filters import ProductFilter, SupplierFilter, MotorcycleCompatibilityFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter

class MotorcycleCompatibilityViewSet(viewsets.ModelViewSet):
    queryset = MotorcycleCompatibility.objects.all()
    serializer_class = MotorcycleCompatibilitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MotorcycleCompatibilityFilter