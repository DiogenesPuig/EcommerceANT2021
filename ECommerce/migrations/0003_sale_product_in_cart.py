# Generated by Django 3.2 on 2021-08-12 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ECommerce', '0002_remove_sale_product_in_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='product_in_cart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ECommerce.productscart'),
        ),
    ]
