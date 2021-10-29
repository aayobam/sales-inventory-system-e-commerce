# Generated by Django 3.2.7 on 2021-10-29 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(blank=True, help_text='16 digit number', max_length=16)),
                ('cvv', models.CharField(blank=True, help_text='3 digit number at the back of your card', max_length=3)),
                ('exp', models.CharField(help_text='Expiry date of card', max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
