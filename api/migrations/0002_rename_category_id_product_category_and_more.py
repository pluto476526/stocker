# Generated by Django 5.1.4 on 2024-12-16 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='supplier_id',
            new_name='supplier',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='warehouse_id',
            new_name='warehouse',
        ),
    ]
