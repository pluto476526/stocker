# api/views.py

from rest_framework import viewsets, status, response, decorators, generics, pagination
from django.db.models import Q, Sum, F, Subquery, OuterRef
from django.contrib.auth.models import User
from accounts.permissions import IsSuperUserOnly
from api.permissions import IsManagerOrReadOnly, IsSuperUserOrReadOnly
from api.mixins import FilterByNameMixin
from api.models import (
    WareHouse,
    Category,
    Product,
    Supplier,
    StockTransaction,
)
from api.serializers import (
    WareHouseSerializer,
    CategorySerializer,
    ProductSerializer,
    SupplierSerializer,
    StockTransactionSerializer,
)
import logging


# Get logger
logger = logging.getLogger(__name__)


class WareHouseViewSet(FilterByNameMixin, viewsets.ModelViewSet):
    """
    Allows superusers and managers to manage warehouses
    """
    queryset = WareHouse.objects.all()
    serializer_class = WareHouseSerializer
    permission_classes = [IsSuperUserOnly]
    pagination_class = pagination.PageNumberPagination

    def create(self, request, *args, **kwargs):
        """
        Adds the manager from the user object
        """
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                id = request.data.get('manager')
                manager = User.objects.get(id=id)
                serializer.save(manager=manager)
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return response.Response(
                {"detail": "Manager with the given ID does not exist"},
                status=status.HTTP_400_BAD_REQUEST
            )


class CategoryViewSet(FilterByNameMixin, viewsets.ModelViewSet):
    """
    Allows superusers to manage categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsSuperUserOrReadOnly]
    pagination_class = pagination.PageNumberPagination


class ProductViewSet(viewsets.ModelViewSet):
    """
    Allows all users to view all available products
    Only warehouse managers can add, edit or delete products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsManagerOrReadOnly]
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        """
        Returns the queryset for filtering
        """
        queryset = super().get_queryset()
        params = self.request.query_params
        filters = Q()

        name = params.get('name')
        category = params.get('category')
        supplier = params.get('supplier')
        warehouse = params.get('warehouse')
        min_price = params.get('min_price')
        max_price = params.get('max_price')
        low_stock = params.get('low_stock')

        if name:
            filters &= Q(name__icontains=name)

        if category:
            filters &= Q(category__name__icontains=category)

        if supplier:
            filters &= Q(supplier__name__icontains=supplier)

        if warehouse:
            filters &= Q(warehouse__name__icontains=warehouse)

        if min_price:
            filters &= Q(price__gte=min_price)

        if max_price:
            filters &= Q(price__lte=max_price)

        if low_stock:
            try:
                threshold = int(low_stock)
                filters &= Q(quantity__lt=threshold)
            except ValueError:
                pass

        return queryset.filter(filters)


    @decorators.action(detail=False, methods=['get'])
    def inventory_report(self, request):
        """
        Generate an overview of the shop
        """
        # Aggregates
        total_inventory_value = Product.objects.aggregate(
            total_value=Sum(F('price') * F('stock_level'))
        )
        total_stock_levels = Product.objects.aggregate(
            total_stock=Sum('stock_level')
        )

        # Categories and their products
        categories = Category.objects.values('id', 'name').annotate(
            products=Subquery(
                Product.objects.filter(category_id=OuterRef('id')).values_list('name', flat=True)
            )
        )

        # Warehouses and their products
        warehouses = WareHouse.objects.values('id', 'name').annotate(
            products = Subquery(
                Product.objects.filter(warehouse_id=OuterRef('id')).values_list('name', flat=True)
            )
        )

        # Restocking and sales history
        restocking_history = StockTransaction.objects.filter(
            transaction_type=StockTransaction.ADD
        ).values('product_id', 'quantity', 'timestamp', 'amount')

        sales_history = StockTransaction.objects.filter(
            transaction_type=StockTransaction.REMOVE
        ).values('product_id', 'quantity', 'timestamp', 'amount')

        # Report response
        report = {
            'total_inventory_value': total_inventory_value['total_value'] or 0,
            'total_stock_count': total_stock_levels['total_stock'] or 0,
            'categories': list(categories),
            'warehouses': list(warehouses),
            'restocking_history': list(restocking_history),
            'sales_history': list(sales_history)
        }
        return response.Response(report, status=status.HTTP_200_OK)


class SupplierViewSet(FilterByNameMixin, viewsets.ModelViewSet):
    """
    Allows superusers to manage suppliers
    """
    queryset = Supplier.objects.all()
    permission_classes = [IsSuperUserOnly]
    serializer_class = SupplierSerializer
    pagination_class = pagination.PageNumberPagination


class StockTransactionListView(generics.ListAPIView):
    """
    Allows superusers to view stock transactions
    """
    queryset = StockTransaction.objects.all()
    permission_classes = [IsSuperUserOnly]
    serializer_class = StockTransactionSerializer
    pagination_class = pagination.PageNumberPagination

    
class StockTransactionDetailView(generics.RetrieveAPIView):
    """
    Allows users to view details of a specific transaction
    """
    queryset = StockTransaction.objects.all()
    permission_classes = [IsSuperUserOnly]
    serializer_class = StockTransactionSerializer
    
