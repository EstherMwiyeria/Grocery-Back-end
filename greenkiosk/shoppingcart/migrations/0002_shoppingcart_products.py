# Generated by Django 4.2.3 on 2023-07-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_product_vendor'),
        ('shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='products',
            field=models.ManyToManyField(to='inventory.product'),
        ),
    ]
