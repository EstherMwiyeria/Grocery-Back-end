# Generated by Django 4.2.3 on 2023-08-04 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0002_shoppingcart_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='total_price',
        ),
    ]
