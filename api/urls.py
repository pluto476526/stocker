# api/urls.py

from django.urls import path, re_path, include
from rest_framework import routers
from api.views import (
    WareHouseViewSet,
    CategoryViewSet,
    SupplierViewSet,
    ProductViewSet,
    StockTransactionListView,
    StockTransactionDetailView,
)

router = routers.DefaultRouter()
router.register(r'warehouses', WareHouseViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('stock-transactions/', StockTransactionListView.as_view()),
    path('stock-transactions/<int:pk>/', StockTransactionDetailView.as_view()),
]
