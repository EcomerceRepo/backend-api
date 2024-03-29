# Generated by Django 4.1.3 on 2023-01-16 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop_api', '0001_initial'),
        ('carts_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='order_items',
            field=models.ManyToManyField(to='carts_api.cartitem'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='favorite_items',
            field=models.ManyToManyField(to='shop_api.product'),
        ),
        migrations.AddField(
            model_name='favorites',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_items',
            field=models.ManyToManyField(to='carts_api.cartitem'),
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
