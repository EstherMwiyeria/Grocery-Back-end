# Generated by Django 4.2.3 on 2023-07-07 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_payment_order_product'),
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='order_number',
        ),
        migrations.AddField(
            model_name='shipping',
            name='order',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
