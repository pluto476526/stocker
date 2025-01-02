# api/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import (
    WareHouse,
    Category,
    Product,
    Supplier,
    StockTransaction,
)


class ManagerSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email']
		
		
class WareHouseSerializer(serializers.ModelSerializer):
    # Foreign key
    # manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(profile__is_staff=True))
    manager_details = ManagerSerializer(source='manager', read_only=True)

    class Meta:
        model = WareHouse
        fields = ['id', 'name', 'location', 'manager_details']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # Foreign Key fields with nested serializers
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    warehouse = serializers.PrimaryKeyRelatedField(queryset=WareHouse.objects.all())

    # Show detailed nested representation
    category_details = CategorySerializer(source='category', read_only=True)
    supplier_details = SupplierSerializer(source='supplier', read_only=True)
    warehouse_details = WareHouseSerializer(source='warehouse', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'category_details',
            'supplier',
            'supplier_details',
            'warehouse',
            'warehouse_details',
            'stock_level',
            'reorder_threshold',
            'timestamp',
            'updated_at',
        ]


class StockTransactionSerializer(serializers.ModelSerializer):
    queryset = Product.objects.all()
    product = serializers.PrimaryKeyRelatedField(queryset=queryset)
    product_detail = ProductSerializer(source='product_id', read_only=True)

    class Meta:
        model = StockTransaction
        fields = [
            'id',
            'product',
            'product_detail',
            'transaction_type',
            'quantity',
            'timestamp',
        ]
