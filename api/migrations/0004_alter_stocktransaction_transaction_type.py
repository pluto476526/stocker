# Generated by Django 5.1.4 on 2024-12-17 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocktransaction',
            name='transaction_type',
            field=models.CharField(choices=[('add', 'add'), ('remove', 'Remove')], max_length=10),
        ),
    ]
