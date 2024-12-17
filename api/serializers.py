# api/serializers.py

from rest_framework import serializers
from api.models import WareHouse, Category, Product, Supplier, StockTransaction


class WareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouse
        fields = '__all__'


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
    category_detail = CategorySerializer(source='category', read_only=True)
    supplier_detail = SupplierSerializer(source='supplier', read_only=True)
    warehouse_detail = WareHouseSerializer(source='warehouse', read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'description',
            'price',
            'category',
            'category_detail',
            'supplier',
            'supplier_detail',
            'warehouse',
            'warehouse_detail',
            'stock_level',
            'reorder_threshold',
            'timestamp',
        ]


class StockTransactionSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
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
