# Generated by Django 5.1.4 on 2024-12-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_stocktransaction_transaction_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocktransaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='stocktransaction',
            name='transaction_type',
            field=models.CharField(choices=[('add', 'add'), ('remove', 'Remove')], max_length=9),
        ),
    ]
