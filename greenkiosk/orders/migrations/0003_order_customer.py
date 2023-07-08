# Generated by Django 4.2.3 on 2023-07-07 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_user'),
        ('orders', '0002_order_payment_order_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    ]
