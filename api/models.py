# api/models.py

from django.db import models, transaction
import logging

# Get logger
logger = logging.getLogger(__name__)


class WareHouse(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    manager = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=20)
    contact_info = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    warehouse = models.ForeignKey(WareHouse, on_delete=models.CASCADE)
    stock_level = models.PositiveIntegerField(default=0)
    reorder_threshold = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Check if stock level is being updated
        if self.pk:
            original = Product.objects.get(pk=self.pk)
            
            if self.stock_level != original.stock_level:    
                delta = self.stock_level - original.stock_level
                transaction_type = (
                    StockTransaction.ADD if delta > 0 else StockTransaction.REMOVE
                )
                
                # Create a stock transaction attomically
                with transaction.atomic():
                    super().save(*args, **kwargs)
                    
                    StockTransaction.objects.create(
                        product_id = self,
                        transaction_type = transaction_type,
                        quantity = abs(delta),
                        amount = int(original.price) * abs(delta)
                    )
                return

        # Save normally if stock level was not edited
        super().save(*args, **kwargs)


class StockTransaction(models.Model):
    ADD = 'add'
    REMOVE = 'remove'

    CHOICES_TYPE = (
        (ADD, 'add'),
        (REMOVE, 'remove'),
    )

    product_id = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    transaction_type = models.CharField(max_length=9, choices=CHOICES_TYPE)
    quantity = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

