# Generated by Django 5.1.4 on 2024-12-17 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_category_id_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='reorder_threshold',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
