# Generated by Django 4.1.3 on 2023-01-09 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0001_initial'),
        ('carts_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='isAbandoned',
        ),
        migrations.RemoveField(
            model_name='order',
            name='isCompleted',
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=0)),
                ('date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_api.product')),
            ],
        ),
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(to='carts_api.cartitem'),
        ),
    ]
