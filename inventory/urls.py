from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet, MotorcycleCompatibilityViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'compatibilities', MotorcycleCompatibilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]