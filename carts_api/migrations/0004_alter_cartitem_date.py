# Generated by Django 4.1.3 on 2023-01-09 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts_api', '0003_rename_products_cart_cart_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]