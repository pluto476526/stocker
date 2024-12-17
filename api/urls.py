# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    WareHouseViewSet,
    CategoryViewSet,
    SupplierViewSet,
    ProductViewSet,
    StockTransactionViewSet,
)


router = DefaultRouter()
router.register(r'warehouses', WareHouseViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'stock-transactions', StockTransactionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
