# Generated by Django 4.1.7 on 2024-01-07 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_remove_order_product_id_remove_order_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
