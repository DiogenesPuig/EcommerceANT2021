# Generated by Django 3.2 on 2021-08-12 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECommerce', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='product_in_cart',
        ),
    ]
