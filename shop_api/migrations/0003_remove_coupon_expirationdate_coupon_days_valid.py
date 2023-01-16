# Generated by Django 4.1.3 on 2023-01-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_api', '0002_rename_dateadded_category_date_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='expirationDate',
        ),
        migrations.AddField(
            model_name='coupon',
            name='days_valid',
            field=models.IntegerField(default=14),
        ),
    ]