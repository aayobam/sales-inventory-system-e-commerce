# Generated by Django 3.2.7 on 2021-10-20 14:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0020_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=10, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]