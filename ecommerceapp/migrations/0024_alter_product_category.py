# Generated by Django 3.2.7 on 2021-10-21 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0023_auto_20211020_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerceapp.category'),
        ),
    ]